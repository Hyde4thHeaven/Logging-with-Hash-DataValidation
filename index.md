## **Logging with Hash and Data Validation**.  

<div align="center"> <img src="cover.png"/> </div>  
  
This is example to write Python for record Log-in logging.  
  
## First, Let's try a simple one.  
Using Python's standard library, **import time** to write down the time that user do a log-in.  
<div align="center"> <img src="log.png" width="100%"/> </div>  
  
## Second, Add Hashing.  
While today most secured database servers do not keep plain text of username and password to prevent the data leak, they keep the data in hashing format, using **import hashlib** and **hash()**, instead. Due to we just testing and we do not create data base yet, so we have to do a little tricky in the checking condition :P.   
<div align="center"> <img src="log+hash.png" width="100%"/> </div>  
However, we think the logging still should to record in plain text because we can see what users trying to log-in. We can use this log to predict or preventing 'Brute Force' things.   
  
## Finally, make more secure with Data Validation.  
Again with Python's standard library, **import re**, we can check a word in the string using **re.search(X, Y)**. Data validation use in prevent script injection and risk of data with imperfections.  
<div align="center"> <img src="log+hash+validate.png" width="100%"/> </div>  
  
**Another secure function is done!** Secured coding is just a flipped hand when you know the hint!
    
## Credit to our team mate:  
Mr.Sakarin Kaewsathitwong and Mr.Sanchat Phaisit
<div align="center"> <img src="https://alfatoxin.github.io/assets/sakarin.png" width="40%"/> &nbsp; &nbsp; &nbsp; <img src="https://ph-sanchat.github.io/mangkorn.jpg" width="40%"/> </div>  

______________________________
<table border="0">
 <tr>
   <td> <h3><i>Although my profile picture is quiet, but the real me can make some noise.</i></h3>
      <hr>
      <b><font color="Blue"> Author: Vuttawat Uyanont </font></b>  <br>
      <font color="grey"><i>Sexiest former engineer & banker who interested in Tech, Sake, and Beer.</i></font>  <br>
      <b>Studying:</b> Master Computer Science in Cybersecurity Management at Mahanakorn University.  <br> </td>  
   <td><img src="Author.png" width="150"/></td>  
 </tr>
</table>
  
