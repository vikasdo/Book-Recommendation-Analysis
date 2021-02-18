# document

[Link to docs](https://drive.google.com/file/d/1tqAixFSWiZiUiY9Yk6qspmzdvjxyqrlM/view?usp=drivesdk)

# colab
https://colab.research.google.com/drive/1W3bnFPMFdxa1ExdYQxuYv43k5QzFrG10
https://colab.research.google.com/drive/18xQP5b_7MjMGtxNl-2XgHtH589J69B-K
# To Setup 

 	 1. Actvate virtual environment
  	git lfs clone url 
	python -m venv env
	env\Scripts\activate
	
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
