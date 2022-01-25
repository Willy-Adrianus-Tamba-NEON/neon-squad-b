from lib2to3.pytree import Base
from unittest import result
from apps.helper import Log
from apps.schemas import BaseResponse
from apps.helper.ConfigHelper import encoder_app
from apps.schemas.SchemaWilly import ResponseDataProvinsi, dataProvinsi
from main import PARAMS
from apps.models.WillyModel import Provinsi

SALT = PARAMS.SALT.salt


class ControllerWilly(object):
    @classmethod
    def get_data_provinsi(cls, limit):
        result = BaseResponse()
        result.status = 400
        countData = Provinsi.get().serialize()

        try:
            if limit is None:
                result.status = 200
                limit = Provinsi.count('provinsi')
                result.message = {"Total Provinsi:": limit}
                Log.info(result.message)
            elif limit <= 0:
                result.status = 404
                result.message = "Limit can't be 0 or below 0"
                Log.info(result.message)
            elif limit > len(countData):
                result.status = 404
                result.message = f"Limit can't be greater than {len(countData)}"
                Log.info(result.message)
            else:
                data = Provinsi.limit(limit).get().serialize()
                result.status = 200
                result.message = "Success"
                result.data = ResponseDataProvinsi(**{'dataprov_list': data})
                Log.info(result.message)

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)
        
        return result

    @classmethod
    def get_data_provinsi_encoded(cls, limit):
        result = BaseResponse()
        result.status = 400
        countData = Provinsi.get().serialize()

        try:
            if limit is None:
                result.status = 200
                limit = Provinsi.count('provinsi')
                result.message = {"Total Provinsi:": limit}
                Log.info(result.message)
            elif limit <= 0:
                result.status = 404
                result.message = "Limit can't be 0 or below 0"
                Log.info(result.message)
            elif limit > len(countData):
                result.status = 404
                result.message = f"Limit can't be greater than {len(countData)}"
                Log.info(result.message)
            else:
                data = Provinsi.limit(limit).get().serialize()
                result.status = 200
                result.message = "Success"
                result.data = encoder_app(ResponseDataProvinsi(**{'dataprov_list': data}).json(), SALT)
                Log.info(result.message)

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)
        
        return result

    @classmethod
    def insert_provinsi(cls, input_data=None):
        input_data = dataProvinsi(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.provinsi is not None:
                Provinsi.insert(input_data)
                data = Provinsi.where('provinsi', '=', input_data.provinsi).get().serialize()
                result.status = 200
                result.message = "Data Inserted"
                result.data = ResponseDataProvinsi(**{'dataprov_list': data})
                Log.info(result.message)
            else:
                result.status = 404
                result.message = "Something happend and API can't insert the data"
                Log.info(result.message)

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)
        
        return result

    @classmethod
    def update_provinsi(cls, provinsi=None, update_data=None):
        result = BaseResponse()
        result.status = 400

        try:
            if provinsi in Provinsi.lists("provinsi"):
                data = Provinsi.where('provinsi', provinsi)
                data.update(update_data)
                result.status = 200
                result.message = f"Updated provinsi: {provinsi}"
                Log.info(result.message)
            else:
                result.status = 404
                result.message = "Data can't be empty"
                Log.info(result.message)

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def delete_provinsi(cls, provinsi):
        result = BaseResponse()
        result.status = 400

        try:
            if provinsi is not None and provinsi in Provinsi.lists("provinsi"):
                data = Provinsi.where('provinsi', '=', provinsi)
                viewDeleted = data.get().serialize()
                data.delete()
                result.status = 200
                result.message = "Provinsi deleted"
                result.data = ResponseDataProvinsi(**{'dataprov_list': viewDeleted})
                Log.info(result.message)
            else:
                result.status = 404
                result.message = "Provinsi is not exists"
                Log.info(result.message)

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

