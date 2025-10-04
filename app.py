from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from werkzeug.utils import secure_filename
import json
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'data-viz-dashboard-key'
app.config['UPLOAD_FOLDER'] = 'data'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls', 'json'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_data(file_path, file_type):
    """Load data from various file formats"""
    try:
        if file_type == 'csv':
            return pd.read_csv(file_path)
        elif file_type in ['xlsx', 'xls']:
            return pd.read_excel(file_path)
        elif file_type == 'json':
            return pd.read_json(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
    except Exception as e:
        raise ValueError(f"Error loading file: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_filename = f"{timestamp}_{filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)

        flash('File uploaded successfully!')
        return redirect(url_for('dashboard', filename=unique_filename))

    flash('Invalid file type. Please upload CSV, Excel, or JSON files.')
    return redirect(request.url)

@app.route('/dashboard/<filename>')
def dashboard(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(file_path):
        flash('File not found')
        return redirect(url_for('index'))

    try:
        file_ext = filename.rsplit('.', 1)[1].lower()
        df = load_data(file_path, file_ext)

        # Get basic data info
        data_info = {
            'filename': filename,
            'rows': len(df),
            'columns': len(df.columns),
            'columns_list': df.columns.tolist(),
            'numeric_columns': df.select_dtypes(include=['number']).columns.tolist(),
            'categorical_columns': df.select_dtypes(include=['object', 'category']).columns.tolist()
        }

        return render_template('dashboard.html', data_info=data_info, filename=filename)

    except Exception as e:
        flash(f'Error processing file: {str(e)}')
        return redirect(url_for('index'))

@app.route('/api/generate_chart/<filename>', methods=['POST'])
def generate_chart(filename):
    data = request.get_json()
    chart_type = data.get('chart_type')
    x_column = data.get('x_column')
    y_column = data.get('y_column')
    color_column = data.get('color_column')

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404

    try:
        file_ext = filename.rsplit('.', 1)[1].lower()
        df = load_data(file_path, file_ext)

        # Generate chart based on type
        if chart_type == 'bar':
            if y_column:
                fig = px.bar(df, x=x_column, y=y_column, color=color_column, title=f"{y_column} by {x_column}")
            else:
                # Count plot for categorical data
                fig = px.bar(df[x_column].value_counts().reset_index(), x='index', y=x_column,
                           title=f"Count of {x_column}")
        elif chart_type == 'line':
            fig = px.line(df, x=x_column, y=y_column, color=color_column, title=f"{y_column} over {x_column}")
        elif chart_type == 'scatter':
            fig = px.scatter(df, x=x_column, y=y_column, color=color_column, title=f"{x_column} vs {y_column}")
        elif chart_type == 'pie':
            fig = px.pie(df, names=x_column, title=f"Distribution of {x_column}")
        elif chart_type == 'histogram':
            fig = px.histogram(df, x=x_column, color=color_column, title=f"Distribution of {x_column}")
        else:
            return jsonify({'error': 'Invalid chart type'}), 400

        # Update layout for better appearance
        fig.update_layout(
            template='plotly_white',
            font_family="Arial",
            title_font_size=16
        )

        return jsonify({'chart': fig.to_json()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)