#!/usr/bin/env python3
# Catálogo espacial: comprobaciones de estructura documental; no certifica corrección científica futura.
from pathlib import Path
import csv, json, sys, re
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def check(condition,detail):
 if not condition: errors.append(detail)
with (ROOT/'catalogo/clases.json').open(encoding='utf-8') as f: cat=json.load(f)
with (ROOT/'catalogo/clases.csv').open(encoding='utf-8-sig',newline='') as f: csv_rows=list(csv.DictReader(f))
with (ROOT/'catalogo/clases.jsonl').open(encoding='utf-8') as f: jsonl=[json.loads(x) for x in f if x.strip()]
check(len(cat)==5120,f'Cantidad de fichas: {len(cat)} vs 5120')
check(len(csv_rows)==len(cat),'CSV difiere en cantidad de filas')
check(len(jsonl)==len(cat),'JSONL difiere en cantidad de registros')
ids=[c['id'] for c in cat]
check(len(set(ids))==len(ids),'IDs duplicados')
check(len({x['titulo'].casefold() for x in cat})==len(cat),'Títulos duplicados sin distinción de contexto curricular')
check([r['id'] for r in csv_rows]==ids,'IDs/orden CSV no coinciden con JSON')
check([r['id'] for r in jsonl]==ids,'IDs/orden JSONL no coinciden con JSON')
check(len([x for x in cat if x['tipo']=='tronco_comun'])==1280,'Conteo formación transversal incorrecto')
check(len([x for x in cat if x['tipo']=='especializacion'])==3840,'Conteo especializaciones incorrecto')
check(all(x['titulo'].strip() and len(x['descripcion_preliminar'])>35 for x in cat),'Falta título o descripción preliminar')
check(all(x['estado']=='solo_titulo_y_referencia_preliminar' for x in cat),'Estado de desarrollo indebidamente alterado')
check(all(len(x['fuentes_preliminares'])>=3 for x in cat),'Ausencia de fuentes iniciales')
check(len(list((ROOT/'programa/tronco-comun').glob('B*.md')))==64,'Faltan índices de bloque')
check(len(list((ROOT/'programa/rutas-profesionales').rglob('R*-M*.md')))==192,'Faltan índices de módulo profesional')
check(len(list((ROOT/'programa/rutas-profesionales').rglob('INDICE.md')))==24,'Faltan índices de ruta profesional')
check(len({x['bloque_id'] for x in cat if x['bloque_id']})==64,'Bloques con clases incompletos')
check(len({x['modulo_id'] for x in cat if x['modulo_id']})==192,'Módulos con clases incompletos')
for bid in {x['bloque_id'] for x in cat if x['bloque_id']}:
 check(len([x for x in cat if x['bloque_id']==bid])==20,f'{bid}: no hay 20 clases')
for mid in {x['modulo_id'] for x in cat if x['modulo_id']}:
 check(len([x for x in cat if x['modulo_id']==mid])==20,f'{mid}: no hay 20 clases')
check((ROOT/'PROGRAMA_ACADEMICO_COMPLETO.md').exists(),'Falta índice completo legible')
check((ROOT/'visor/index.html').exists(),'Falta visor local')
for key in ['titulo','descripcion_preliminar','fuentes_preliminares','numero_clase','id']:
 check(all(key in x for x in cat),f'Falta campo {key} en fichas')
print('Catálogo:',len(cat),'clases | 64 bloques | 24 rutas | 192 módulos')
if errors:
 print('VALIDACIÓN CON ERRORES:',len(errors))
 for e in errors: print('-',e)
 sys.exit(1)
print('VALIDACIÓN DOCUMENTAL APROBADA (no implica clases desarrolladas).')
