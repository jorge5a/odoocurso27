from odoo import models, fields

class Libro(models.Model):
    _name = 'mi_biblioteca.libro'   
    _description = 'Modelo para representar un libro en la biblioteca'

    name = fields.Char(string='Título', required=True)
    autor = fields.Char(string='Autor', required=True)
    fecha_publicacion = fields.Date(string='Fecha de Publicación')
    paginas = fields.Integer(string='Número de Páginas')
    disponible = fields.Boolean(string='Disponible', default=True)
