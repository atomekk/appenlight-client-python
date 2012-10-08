from errormator_client.utils import import_module, deco_func_or_method
from errormator_client.timing import time_trace, import_from_module, _e_trace

def add_timing(min_duration=0.05):
    module = import_module('mako')
    if not module:
        return
    
    from mako import template
    
    def gather_template(template, *args, **kwargs):
        return {'type':'template',
                'statement':'render_mako',
                'parameters':''}
        
    if hasattr(template.Template, '_e_attached_wrapper'):
        return
    deco_func_or_method(template, 'Template.render', time_trace,
                          gather_template, min_duration, is_template=True)
    deco_func_or_method(template, 'Template.render_unicode', time_trace,
                          gather_template, min_duration, is_template=True)
    deco_func_or_method(template, 'Template.render_context', time_trace,
                          gather_template, min_duration, is_template=True)