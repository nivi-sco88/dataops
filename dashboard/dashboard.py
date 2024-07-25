from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Read the processed data
    df = pd.read_csv('processed_data.csv')
    
    # Generate some summary statistics
    total_sales = df['TotalSales'].sum()
    total_invoices = df['InvoiceNo'].nunique()
    total_customers = df['CustomerID'].nunique()
    
    return render_template('index.html', 
                           tables=[df.head().to_html(classes='data', header="true")], 
                           total_sales=total_sales, 
                           total_invoices=total_invoices, 
                           total_customers=total_customers)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
