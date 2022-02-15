# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class garaje(models.Model):
#     _name = 'garaje.garaje'
#     _description = 'garaje.garaje'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

class coche(models.Model):
	_name = 'garaje.coche'
	_description = 'model coche'

	name = fields.Char('Id',required=True)
	modelo = fields.Char(string='Modelo',required=True)

	#relaciones
	fabricante_id=fields.Many2many('garaje.fabricante',string='Fabricante')


class fabricante(models.Model):
	_name = 'garaje.fabricante'
	_description = 'model fabricante'

	name = fields.Char('Id',required=True)
	empresa = fields.Char(string='Empresa',required=True)

	#relaciones
	persona_id=fields.Many2one('garaje.persona',string='Persona')
	coche_ids=fields.Many2many('garaje.coche','fabricante_id',string='Fabricante del coche')


class persona(models.Model):
	_name = 'garaje.persona'
	_description = 'model persona'

	name = fields.Char('Dni',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	fecha_nacimiento = fields.Date(string="Fecha de nacimiento",required=True)

	#relaciones
	persona_ids=fields.One2many('garaje.fabricante', 'persona_id',string='Dni del fabricante')
	persona_ids2=fields.One2many('garaje.cliente', 'cliente_id',string="Dni del cliente")
	persona_ids3=fields.One2many('garaje.empleado', 'empleado_id',string="Dni del empleado")



class cliente(models.Model):
	_name = 'garaje.cliente'
	_description = 'model cliente'

	name = fields.Char('Id',required=True)
	plaza = fields.Integer(string='Plaza',required=True)

	#relaciones 
	cliente_id= fields.Many2one('garaje.persona',string='Persona')
	factura_ids = fields.One2many('garaje.lin_fac', 'cliente_id', string='Linea Factura')


class factura(models.Model):
	_name = 'garaje.factura'
	_description = 'model factura'

	name = fields.Char('Id', required = True)
	costo_fac = fields.Integer(string='Coste Factura', required = True)
	tipo_fac = fields.Char(string='Tipo de la factura', required = True)

	#relaciones
	factura_ids = fields.One2many('garaje.lin_fac', 'factura_id', string = 'Linea Factura')


class lin_fac(models.Model):
	_name = 'garaje.lin_fac'
	_description = 'model lin_fac'

	name = fields.Char('Codigo', required = True)
	
	#relaciones
	factura_id = fields.Many2one('garaje.factura', string = 'Factura')
	cliente_id = fields.Many2one('garaje.cliente', string = 'Cliente')


class empleado(models.Model):
	_name = 'garaje.empleado'
	_description = 'model empleado'

	name = fields.Char('Codigo Empleado', required = True)

	
	#relaciones
	empleado_id= fields.Many2one('garaje.persona',string='Persona')
	trabajo_ids = fields.Many2many('garaje.trabajo','empleado',string='Empleado')
	herramienta_ids = fields.Many2many('garaje.herramientas','empleado_asignado',string='Herramienta')



class trabajo(models.Model):
	_name = 'garaje.trabajo'
	_description = 'model trabajo'

	name = fields.Char('Nombre trabajo', required = True)
	sueldo = fields.Integer('Sueldo', required = True)

	
	#relaciones
	empleado= fields.Many2many('garaje.empleado',string='Empleado')


class herramientas(models.Model):
	_name = 'garaje.herramientas'
	_description = 'model herramientas'

	name = fields.Char('Codigo herramienta', required = True)
	cantidad = fields.Integer('Cantidad', required = True)

	
	#relaciones
	empleado_asignado= fields.Many2many('garaje.empleado',string='Empleado asignado')

