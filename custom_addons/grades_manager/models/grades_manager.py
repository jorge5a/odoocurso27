from odoo import models, fields

class GradesCourse(models.Model):
    _name = 'grades.course'
    _description = 'Modelo para representar un curso'

    name = fields.Char(string='Nombre del Curso', required=True)
    student_qty = fields.Integer(string='Cantidad de Estudiantes')
    grades_average = fields.Float(string='Promedio de Calificaciones')
    is_active = fields.Boolean(string='Activo', default=True)
    course_start_date = fields.Date(string='Fecha de Inicio del Curso')
    course_end_date = fields.Date(string='Fecha de Fin del Curso')
    last_evaluation_date = fields.Datetime(string='Última Fecha de Evaluación')
    couse_image = fields.Binary(string='Imagen del Curso')
    course_shift = fields.Selection([
        ('morning', 'Mañana'),
        ('afternoon', 'Tarde'),
        ('evening', 'Noche')
    ], string='Turno del Curso',
    )
   