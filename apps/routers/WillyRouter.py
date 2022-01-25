from asyncio.windows_events import NULL
import json
from typing import Optional
from unittest import result
from fastapi import APIRouter, Body, Response
from apps.controllers.WillyController import ControllerWilly as willy

router = APIRouter()

# Deklarasi Example

insert_example = json.dumps({
    "provinsi": "",
    "ibu_kota_wilayah": "",
    "luas_wilayah": "",
    "persentase_terhadap_luas_wilayah": "",
    "jumlah_pulau": "",
}, indent=2)

update_example = json.dumps({
    "provinsi": "",
    "ibu_kota_wilayah": "",
    "luas_wilayah": "",
    "persentase_terhadap_luas_wilayah": "",
    "jumlah_pulau": "",
}, indent=2)


# Router endpoint

@router.get("/get_data_provinsi")
async def get_data_provinsi(response: Response, limit:Optional[int]=None):
    result = willy.get_data_provinsi(limit)
    response.status_code = result.status
    return result

@router.get("/get_data_provinsi_encoded")
async def get_data_provinsi_encoded(response: Response, limit:Optional[int]=None):
    result = willy.get_data_provinsi_encoded(limit)
    response.status_code = result.status
    return result

@router.post("/insert_data_provinsi")
async def insert_provinsi(response: Response, input_data=Body(..., example=insert_example)):
    result = willy.insert_provinsi(input_data)
    response.status_code = result.status
    return result

@router.put("/update_data_provinsi")
async def update_provinsi(response: Response, provinsi: str, input_data=Body(..., example=update_example)):
    result = willy.update_provinsi(provinsi, input_data)
    return result

@router.delete("/delete_data_provinsi")
async def delete_provinsi(response: Response, provinsi: str):
    result = willy.delete_provinsi(provinsi)
    return result

