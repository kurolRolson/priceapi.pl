import json
import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    url = "https://allegro.pl/listing?string=smartwatch&limit=20"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    r = requests.get(url, headers=headers, timeout=30)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    products = []
    # Allegro selectors (updated)
    items = soup.select('.mp-ProductCard, [data-testid*="ProductCard"]')
    for item in items[:5]:
        name = item.select_one('[data-testid*="name"], h2 a, .offer-title')
        price = item.select_one('[data-testid*="price"], .offer-price, .mp-PriceBox__price')
        if name and price:
            products.append({
                'name': name.get_text().strip()[:50],
                'price': price.get_text().strip()
            })
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Allegro scraper v1',
            'count': len(products),
            'products': products
        })
    }
