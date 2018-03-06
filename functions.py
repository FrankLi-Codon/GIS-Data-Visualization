'''function to return county from serach term'''

def find_county(serach_list):
    import geocoder
    serach_result = geocoder.bing(serach_list, method = 'batch')
    county_list = [i.county for i in serach_result]
    county_dict = {zip(serach_list, county_list)}
    return county_dict
