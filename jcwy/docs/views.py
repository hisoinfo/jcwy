from rest_framework_swagger.docgenerator import DocumentationGenerator as _DocumentationGenerator
from rest_framework_swagger.views import SwaggerApiView
from rest_framework.views import Response
from rest_framework_swagger.introspectors import get_resolved_value
import markdown2
import sys

def trim(docstring):
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxint
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxint:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)




class DocumentationGenerator(_DocumentationGenerator):
    def _get_serializer_fields(self, serializer):
        """
        Returns serializer fields in the Swagger MODEL format
        """
        if serializer is None:
            return

        fields = serializer().get_fields()

        data = {}
        for name, field in fields.items():

            data[name] = {
                'type': field.type_label,
                'required': getattr(field, 'required', None),
                'help_text': getattr(field, 'help_text', None),
                'allowableValues': {
                    'min': getattr(field, 'min_length', None),
                    'max': getattr(field, 'max_length', None),
                    'defaultValue': get_resolved_value(field, 'default', None),
                    'readOnly': getattr(field, 'read_only', None),
                    'valueType': 'RANGE',
                }
            }
        return data


class DocsApiView(SwaggerApiView):

    def get(self, request, path):
        apis = self.get_api_for_resource(path)
        generator = DocumentationGenerator()
        api_docs = generator.generate(apis)
        '''
        for api in api_docs:
                for operation in api['operations']:
                        if operation['notes']:
				operation['notes'] = trim(operation['notes'].replace("<br/>", "\n"))
                                if isinstance(operation['notes'], unicode):
                                        operation['notes'] = markdown2.markdown(operation['notes'],extras=["wiki-tables"])
                                else:
                                        operation['notes'] = markdown2.markdown(unicode(operation['notes'], 'utf8'),extras=["wiki-tables"])
        '''
        return Response({
            'apis': api_docs,
            'models': generator.get_models(apis),
            'basePath': self.api_full_uri.rstrip('/'),
        })
