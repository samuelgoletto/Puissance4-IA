# Connect 4 VS AI

## REST Service

### Setup (dependencies)
```bash
python3 -m pip install fastapi
python3 -m pip install uvicorn[standard]
```

### Launch service

* Be at the project root
```bash
uvicorn game.service:app --reload
```

### Endpoint

* Check console to get the endpoint
  * Usually `http://127.0.0.1:8000/`


## Interactive game experience

* Be at the project root
```bash
python3 -m game.main
```

* In "*game.ai.strategies*", you can tweak the `MIN_MAX_STRATEGY_DEPTH` value to make the IA think harder
  * Depth can go from 2 to 5+, and it is beginning to get slow after 7