# Copyright 2021 VyOS maintainers and contributors <maintainers@vyos.io>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.

from ariadne import SchemaDirectiveVisitor, ObjectType
from . queries import *
from . mutations import *

def non(arg):
    pass

class ngNOSDirective(SchemaDirectiveVisitor):
    def visit_field_definition(self, field, object_type, make_resolver=non):
        name = f'{field.type}'
        # field.type contains the return value of the mutation; trim value
        # to produce canonical name
        name = name.replace('Result', '', 1)

        func = make_resolver(name)
        field.resolve = func
        return field

class ConfigSessionQueryDirective(ngNOSDirective):
    """
    Class providing implementation of 'configsessionquery' directive in schema.
    """
    def visit_field_definition(self, field, object_type):
        super().visit_field_definition(field, object_type,
                                       make_resolver=make_config_session_query_resolver)

class ConfigSessionMutationDirective(ngNOSDirective):
    """
    Class providing implementation of 'configsessionmutation' directive in schema.
    """
    def visit_field_definition(self, field, object_type):
        super().visit_field_definition(field, object_type,
                                       make_resolver=make_config_session_mutation_resolver)

class GenOpQueryDirective(ngNOSDirective):
    """
    Class providing implementation of 'genopquery' directive in schema.
    """
    def visit_field_definition(self, field, object_type):
        super().visit_field_definition(field, object_type,
                                       make_resolver=make_gen_op_query_resolver)

class GenOpMutationDirective(ngNOSDirective):
    """
    Class providing implementation of 'genopmutation' directive in schema.
    """
    def visit_field_definition(self, field, object_type):
        super().visit_field_definition(field, object_type,
                                       make_resolver=make_gen_op_mutation_resolver)

class CompositeQueryDirective(ngNOSDirective):
    """
    Class providing implementation of 'system_status' directive in schema.
    """
    def visit_field_definition(self, field, object_type):
        super().visit_field_definition(field, object_type,
                                       make_resolver=make_composite_query_resolver)

class CompositeMutationDirective(ngNOSDirective):
    """
    Class providing implementation of 'system_status' directive in schema.
    """
    def visit_field_definition(self, field, object_type):
        super().visit_field_definition(field, object_type,
                                       make_resolver=make_composite_mutation_resolver)

directives_dict = {"configsessionquery": ConfigSessionQueryDirective,
                   "configsessionmutation": ConfigSessionMutationDirective,
                   "genopquery": GenOpQueryDirective,
                   "genopmutation": GenOpMutationDirective,
                   "compositequery": CompositeQueryDirective,
                   "compositemutation": CompositeMutationDirective}
