# pns_m1_2025

## How to run this project (for mac, for windows ask Nojus)

1. Create virtual environment

```
python -m venv venv
```
or
```
python3 -m venv venv
```

2. Activate the virtual environment
```
source venv/bin/activate
```

3. Install required libraries
```
pip install -r requirements.txt 
```
or
```
pip3 install -r requirements.txt 
```

4. Check status and Add changes 
```
git status
git add .
```

5. Commit changes
```
git commit -a -m 'some message'
```

6. Push changes
```
git push
```

7. Pull changes
```
git pull
```



## Extras
1. Collect libraries in requirements.txt (after creating a venv)
```
pip install pipreqs
pipreqs ./
```