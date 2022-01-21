from fastapi import FastAPI
from inputname import funcname
from summ import funcsumm
from reversword import funcreversword
from paritystring import funcparitystr
from age import funcage
from codeinstr import funccode
from extent import funcextent
from quadequation import funcquad
from lenstring import funclenstr
from rubcoin import funcrub, funccoin
from suppmain import funcmain
from summcond import funcsummcond
from acumm import funcaccum
from fastapi import Response
app = FastAPI()



@app.get("/3_1/{string}")
async def handler(string):
    result = funcname(string)
    return {"result": {result}}

@app.get("/3_2/{int_a}/{int_b}")
async def handler(int_a: int, int_b: int):
    result = funcsumm(int_a, int_b)
    return {"result": {result}}

@app.get("/3_3/{word_a}/{word_b}")
async def handler(word_a: str, word_b: str):
    result = funcreversword(word_a, word_b)
    return {"result": result}

@app.get("/3_4/{string}")
async def handler(string: str):
    result = funcparitystr(string)
    return {"result": result}

@app.get("/3_5/{int}")
async def handler(int: float):
    result = funcage(int)
    return {"result": result}

@app.get("/3_6/{string}")
async def handler(string: str):
    result = funccode(string)
    return {"result": result}

@app.get("/3_7/{integ}")
async def handler(integ):
    result = funcextent(integ)
    return {"result": result}

@app.get("/3_8/{a}/{b}/{c}")
async def handler(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    result = funcquad(a, b, c)
    return {"result": result}

@app.get("/3_9/{string}")
async def handler(string):
    result = funclenstr(string)
    return {"result": result}

@app.get("/3_10/{rub}/{coin}")
async def handler(rub, coin):
    result_1 = funcrub(rub)
    result_2 = funccoin(coin)
    return {"result": [result_1, result_2]}

@app.get("/3_11/{mail}")
async def handler(mail):
    result = funcmain(mail)
    return {"result": result}

@app.get("/4_1/{list}")
async def handler(list):
    result = funcsummcond(list)
    return {"result": result}



@app.get("/4_2/{list}")
async def handler(list):
    if list == 'stop':
        return {"result": "Exiting the function"}
    result = funcaccum(list)
    return {"result": result}
