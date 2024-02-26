# Home Library Organizer
Barcode reader to implement at home.

## Data Base
```
Status: Manually Edited from Excel. 
Goals : introduce information from interface
```

As start point, the data base used in this project is created manually and using books at home.

Data is organized by the following criteria :
* Author last name
* Author Name
* Title
* Status
* Code
* Barcode


To create the barcode, the font IDAtomationHC39 is used. Can find it [here](https://www.dafont.com/es/idautomationhc39m.font)
Logic: first letters from all the information described and number if is a repeated pattern.

> Example :

| LAST NAME  |    NAME   |   TITLE    |    CODE    |
| :---: | :---: | :---: | :---: |
| AUSTEN     |    JANE   |   EMMA     |    AJE0    |




And the tutorial from [Excel Tutorials by EasyClick Academy](https://www.youtube.com/watch?v=oOLDS5vo79I) was referenced. 


## Barcode Reader

```
Status: Reads/decodes  from .png formats
Goals: Create a Camera interface to read code and let user know information from data base
```

Barcode Decoder Code was obtained at [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-make-a-barcode-reader-in-python/)

To better functionality install the libraries or dependencies listed below.

* Pandas
* pyzbar
* openCV-python
* openpyxl

  
