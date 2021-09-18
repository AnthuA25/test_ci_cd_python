from flask_restful import Resource, reqparse


class ActividadesController(Resource):
    def get(self):
        return{
            "message":None,
            "content": [{
                "actividadId":1,
                "actividadNombre":"Ir a la playa"
            },
            {
                "actividadId":2,
                "actividadNombre":"Cocinar"
            },
            {
                "actividadId":3,
                "actividadNombre":"Ir al cumpleaños de mi abuelita"
            }]
        }, 201