# Real State Prices Research

## Business Problem
A real state company wants to know what is the average price of apartments and houses in São Paulo city.

## Tools used

### Languages
- Python 
- SQL;
- HTML;
- CSS;
- Javascript.

### Libraries and Frameworks
- Selenium

### Cloud
- Microsoft Azure;

### Versioning
- Git; 
- Github.

### Website Hosting
- GitHub Pages.

## Resources

### APIs
- IBGE: https://servicodados.ibge.gov.br/api/v1/localidades/municipios/3550308/distritos

### Websites to be Scrapped
- ZAP IMOVEIS: https://www.zapimoveis.com.br/
- Imovel WEB: https://www.imovelweb.com.br/

### Courses
- UDEMY | Automate Everything with Python: https://thoughtworks.udemy.com/course/automate-everything-with-python/

## Roadmap

- [X] Find an API that contains the districts São Paulo, SP;
  - Both the name and the region of the city.
- [X] Collect the districts, process them and add them to a CSV file;
- [ ] Store the file in the cloud;
- [X] Choose one or more real estate websites;
- [X] Extract the necessary data for analysis and put them in CSV files; 
  - [ ] Type of residence;
  - [X] District;
  - [X] Price.
- [ ] Store the files in the cloud;
- [ ] Make the process recurrent until the limit of 100 residences is reached;
- [ ] Access the data in the cloud;
- [ ] Process them; 
  - Standardize; 
  - Segregate by districts; 
  - Calculate the average.
- [ ] Create an API to make the data available;
- [ ] Create a website to make the data available;
  - Create a table to visualize them;