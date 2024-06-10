from flask import jsonify, current_app
from .scraper import scrape_news


@current_app.route('/scrape', methods=['GET'])
def scrape_and_save():
    try:
        print("Iniciando raspagem e salvamento de notícias...")
        news = scrape_news()
        print("Notícias raspadas:", news)
        return jsonify({'message': 'News scraped and saved successfully', 'news': news}), 200
    except Exception as e:
        current_app.logger.error("Erro ao raspar as notícias: %s", e)
        return jsonify({'message': 'Erro ao raspar as notícias'}), 500
