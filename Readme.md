# Web Scraping & Visualisation

This is a Scrapy project to scrape Id, Height, Weight & Gender of celebrities/sportsperson from https://healthyceleb.com.

This project is only meant for educational purposes.


## Extracted data

This project extracts ID, Gender, Height, Weight combined with the respective celebrity/player's names and their profile's url. The extracted data looks like this sample:


```bash
{
     'Id': '83277',
 	 'gender': 'Female',
 	 'height': ['5 ft 2 in or 157.5 cm'],
     'name': ['Alexa Paige Scimeca'],
     'url': 'https://healthyceleb.com/alexa-scimeca-knierim-height-weight-age-body-statistics/83277',
     'weight': ['45 kg or 99 lbs']
}
```

## Spiders

This project contains one spider: ```celeb```

## Scraping the website

Start the crawling by running the following command:

``` $ scrapy crawl celeb ```

## Scraped Data Cleaning

So the scraped data is going to be used for the visualisation part. Thus, it has to be normalised and cleaned.

Example:

```Height of some celeb is in feet-inches format, for some it is in centimeters and some profiles have ½ in their height data. Therefore, normalising height to centimeters.```

```Weight data is having 'Kg' text in it. So, removing the text and keeping the number only.```

For Cleaning the data, there is a file named ``` cleaner.py ```

Run this file and it would generate ``` Fin.csv``` file after completing the data cleaning & wrangling process.

## Data Visualisation 

Would suggest you to use ``` Jupyter Notebook``` for this part. 

Screenshots of the visualisations: 

![Alt text](/screenshots/1.png?raw=true)

![Alt text](/screenshots/2.png?raw=true)

![Alt text](/screenshots/3.png?raw=true)

![Alt text](/screenshots/4.png?raw=true)

![Alt text](/screenshots/5.png?raw=true)

![Alt text](/screenshots/6.png?raw=true)

![Alt text](/screenshots/7.png?raw=true)
     



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.