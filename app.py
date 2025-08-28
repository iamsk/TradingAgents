from flask import Flask, render_template_string
from flask_cors import CORS

from mdb import table

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>报告列表</title>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial; max-width: 800px; margin: 50px auto; padding: 20px; }
        h1 { color: #333; border-bottom: 2px solid #4CAF50; padding-bottom: 10px; }
        .report { background: #f5f5f5; margin: 10px 0; padding: 15px; border-radius: 5px; 
                  transition: all 0.3s; border-left: 4px solid #4CAF50; }
        .report:hover { background: #e8f5e9; transform: translateX(5px); }
        .report a { text-decoration: none; color: #2196F3; font-weight: bold; font-size: 18px; }
        .report a:hover { color: #1976D2; }
        .date { color: #666; font-size: 14px; margin-top: 5px; }
        .add-btn { background: #4CAF50; color: white; padding: 10px 20px; border: none; 
                   border-radius: 5px; cursor: pointer; margin: 20px 0; }
        .add-btn:hover { background: #45a049; }
    </style>
</head>
<body>
    <h1>📊 报告中心</h1>
    <div id="reports">
        {% for report in reports %}
        <div class="report">
            <a href="{{ report.url }}" target="_blank">{{ report.ticker }}</a>
            <div class="date">📅 {{ report.analysis_date }}</div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
'''


@app.route('/')
def index():
    sort = [(u"analysis_date", -1), (u"ticker", 1)]
    records = table.find({}, sort=sort)
    # print(len(reports))
    # reports = [{'url': 'https://reports.askpic.com/SBET/2025-08-27/reports/final_trade_decision.md', 'title': 'SBET',
    #             'date': '2025-08-27'}]
    reports = []
    for report in records:
        url = f'https://ta.askpic.com/reports/{report["ticker"]}/{report["analysis_date"]}/reports/final_trade_decision.md'
        reports.append({"url": url, 'ticker': report['ticker'], 'analysis_date': report["analysis_date"]})
    return render_template_string(HTML_TEMPLATE, reports=reports)


if __name__ == '__main__':
    app.run(port=8009, debug=True)
