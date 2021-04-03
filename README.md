![logo](https://github.com/vikasdo/Book-Recommendation-Analysis/blob/main/bookstore/static/img/logo.PNG)

# Theme approach ![](https://warehouse-camo.ingress.cmh1.psfhosted.org/582ab2eba9d0e0f4acbea2fd883f604349908147/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f74656e736f72666c6f772e7376673f7374796c653d706c6173746963)
<img align="right" src="https://media.giphy.com/media/l0HlESqXkgB97Xs7C/giphy.gif" width = "200" height = "250">
Today, the growth of technology has enabled everyone to make and buy items online. The E-commerce industry is expected to rise in the coming years and so there is a need for an efficient E-commerce recommendation system which suggests products to users .In our project, we try to recommend products to authors, publishers and retailers by providing them with personalized feedback from user reviews. The retailers can also analyze the top trending books and focus on personalization for users or provide them with exciting offers which can motivate the user to make more purchases. We also provide a Heat map of users and give recommendations based on the demographic features also. So, in this Way the retailer gets more profits by understanding the customer and focusing on their purchase pattern.
# Document

[Link to docs](https://drive.google.com/file/d/1f7TCuBrfeaU62j1wUKqRqG286XLAtAC8/view?usp=sharing)

# Google Colab Links
https://colab.research.google.com/drive/1W3bnFPMFdxa1ExdYQxuYv43k5QzFrG10
https://colab.research.google.com/drive/18xQP5b_7MjMGtxNl-2XgHtH589J69B-K

# To Setup 

 	 1. Actvate virtual environment
  	
	python -m venv env
	env\Scripts\activate
	2.Install git lfs : 
	git lfs install
  	pip install -r requirements.txt
	python main.py
	
# To run 
	Activate 
	source env/bin/activate
	python main.py

# Db Migrate
```
python manager.py db init
python manager.py db migrate
python manager.py db upgrade
```
# Website Demo
<h3>CUSTOMER SITE</h3> 
<img src="bookstore/README_DEMO.gif" alt="Demo" width="80%" height="90%"/> 
<h3>RETAILER SITE</h3>
<img src="https://user-images.githubusercontent.com/68437435/111871736-bc854780-89b1-11eb-9614-455e615025ae.gif" alt="Demo" width="80%" height="90%"/>
<img src="https://user-images.githubusercontent.com/68437435/111871719-a8414a80-89b1-11eb-87c0-0a3288a34add.gif" alt="Demo" width="80%" height="90%"/>
</p>

<h3>Scan the below QR to visit the Website</h3>
<img src="https://github.com/vikasdo/Book-Recommendation-Analysis/blob/main/bookstore/static/img/qrcode_booklystore.herokuapp.com.png" width="200px" height="200px"/>
<a href="https://booklystore.herokuapp.com/login" style="text-decoration:none; color:white;">Bookly Store</a>

# Contribution Guidelines🏗

Are we missing any of your favorite features, which you think you can add to it❓ We invite you to contribute to this project and improve it further

## To start contributing, follow the below guidelines: 

**1.**  Fork [this](https://github.com/vikasdo/Book-Recommendation-Analysis.git) repository.

**2.**  Clone your forked copy of the project.

```
git clone https://github.com/<your_user_name>/Book-Recommendation-Analysis.git
```


**3.** Navigate to the project directory :file_folder: .

```
cd Book-Recommendation-Analysis
```

**4.** Add a reference(remote) to the original repository.

```
git remote add upstream https://github.com/vikasdo/Book-Recommendation-Analysis.git
```

**5.** Check the remotes for this repository.

```
git remote -v
```

**6.** Always take a pull from the upstream repository to your master branch to keep it at par with the main project(updated repository).

```
git pull upstream main
```

**7.** Create a new branch.

```
git checkout -b <your_branch_name>
```

**8.** Perform your desired changes to the code base.

<p align="center"><img width=35% src="https://media2.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif?cid=ecf05e47pzi2rpig0vc8pjusra8hiai1b91zgiywvbubu9vu&rid=giphy.gif"></p>

**9.** Track your changes:heavy_check_mark: .

```
git add . 
```

**10.** Commit your changes .

```
git commit -m "Relevant message"
```

**11.** Push the committed changes in your feature branch to your remote repo.

```
git push -u origin <your_branch_name>
```

**12.** To create a pull request, click on `compare and pull requests`. Please ensure you compare your feature branch to the desired branch of the repo you are suppose to make a PR to.


**13.** Add appropriate title and description to your pull request explaining your changes and efforts done.


**14.** Click on `Create Pull Request`.

## The geek🤓 behind this initiative:

<table>
  <tr>
    <td align="center"><a href="https://github.com/vikasdo"><img src="https://avatars.githubusercontent.com/u/44545660?s=400&u=eeb8f17ce2c96e0e37b075b56218284a47589c40&v=4" width="100px;" alt=""/><br /><sub><b>Vikas</b></sub></a><br /></td>
  </tr>
</table>

## Book Recommendation System is a part of these open source programs:

<p align="center">
 <a>
 <img  width="70%" height="30%" src="https://raw.githubusercontent.com/GirlScriptSummerOfCode/MentorshipProgram/master/GSsoc%20Type%20Logo%20Black.png">

 
</p>

</br>

# Contributors👨‍💻👩🏽‍💻

#### Thanks to these wonderful people 🙌
✨✨✨
<table>
	<tr>
		<td>
   <a href="https://github.com/vikasdo/Book-Recommendation-Analysis/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=vikasdo/Book-Recommendation-Analysis" />
</a>
		</td>
	</tr>
</table>
✨✨✨
