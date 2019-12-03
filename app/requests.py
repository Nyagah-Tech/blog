import urllib.request,json
from .models import Quote

base_url = 'http://quotes.stormconsultancy.co.uk/random.json' 

def get_quotes():
    get_quote_url = base_url

    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_results = None

        if get_quote_response:
            quote_list = get_quote_response
            quote_results = process_results(quote_list)
    return quote_results

def process_results(quote_list):
    quote_results = []


    author = quote_list.get('author')
    quote = quote_list.get('quote')

    quoteArr = Quote(author,quote)
    quote_results.append(quoteArr)
    return quote_results
