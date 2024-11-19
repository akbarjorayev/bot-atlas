from countryinfo import CountryInfo


def get_country_data(country_name):
    data = CountryInfo(country_name).info()

    population = data["population"]
    area = data["area"]
    res = f"""
Facts about <b>{data['name']}</b>

Official Name: {data['name']}
Native Name: {data['nativeName']}
Region: {data['region']}
Subregion: {data['subregion']}
Capital: {data['capital']}
Population: {f'{population:,}'.replace(",", ".")} people
Area: {f'{area:,}'.replace(",", ".")} km²
Currency: {data['currencies'][0]}
Call code: +{data['callingCodes'][0]}
Time zone: {', '.join(data['timezones'])}

More information: {data['wiki']}
    """
    return res
