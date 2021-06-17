from tweebo_parser import API, ServerError
# Assumes server is running locally at 0.0.0.0:8000
tweebo_api = API()
text_data = ['Guangdong University of Foreign Studies is located in Guangzhou.',
             'Lucy is in the sky with diamonds.']
try:
    # result_stanford = tweebo_api.parse_stanford(text_data)
    result_conll = tweebo_api.parse_conll(text_data)
except ServerError as e:
    print(f'{e}\n{e.message}')

print('parse done!')
for result in result_conll:
	print(result)
	print('====')