import json

lucros_json = '''
{
"faturamentoDiario":[
{"dia":1,"valor":22174.0},
{"dia":2,"valor":24537.0},
{"dia":3,"valor":26139.0},
{"dia":4,"valor":0.0},
{"dia":5,"valor":0.0},
{"dia":6,"valor":26742.0},
{"dia":7,"valor":0.0},
{"dia":8,"valor":42889.0},
{"dia":9,"valor":14161.0},
{"dia":10,"valor":0.0},
{"dia":11,"valor":2000.0},
{"dia":12,"valor":9000.0},
{"dia":13,"valor":7800.0},
{"dia":14,"valor":3205.0},
{"dia":15,"valor":0.0}
]
}'''

lucros = json.loads(lucros_json)
faturamentoDiario = lucros['faturamentoDiario']

faturamentoValido = [dia['valor'] for dia in faturamentoDiario if dia['valor'] > 0]

faturamentoMenor = min(faturamentoValido)
faturamentoMaior = max(faturamentoValido)


print(f"o menor: {faturamentoMenor}, o maior: {faturamentoMaior}") # 0.0 42889.0 (faturamentoMenor)

