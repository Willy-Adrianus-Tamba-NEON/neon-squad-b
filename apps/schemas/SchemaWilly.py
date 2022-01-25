from datetime import date
import email
from pydantic import BaseModel
from typing import Optional, List


class dataProvinsi(BaseModel):
    provinsi: str = None
    ibu_kota_wilayah: str = None
    luas_wilayah: str = None
    persentase_terhadap_luas_wilayah: str  = None
    jumlah_pulau: str  = None

class ResponseDataProvinsi(BaseModel):
    dataprov_list: List[dataProvinsi]

