# coding=utf-8
"""
Package provides functionality for importing from BPMN-E2 XML to graph representation
"""
from xml.dom import minidom

import bpmn_python.bpmn_import_utils as utils
import bpmn_python.bpmn_python_consts as consts
import bpmn_python.bpmn_diagram_import as bpmn_import


class BpmnE2DiagramGraphImport(object):
    """
    Class BPMNDiagramGraphImport provides methods for importing BPMN-E2 XML file.
    As a utility class, it only contains static methods. This class is meant to be used from BPMNE2DiagramGraph class.
    """

    def __init__(self):
        pass

    @staticmethod
    def load_diagram_from_xml(filepath, bpmn_e2_diagram):
        """
        Reads an XML file from given filepath and maps it into inner representation of BPMN-E2 diagram.
        Returns an instance of BPMNE2DiagramGraph class.

        :param filepath: string with output filepath,
        :param bpmn_e2_diagram: an instance of BpmnE2DiagramGraph class.
        """

        """ Normal BPMN import """
        bpmn_import.BpmnDiagramGraphImport.load_diagram_from_xml(filepath, bpmn_e2_diagram)

        """ 
        TODO extend the above representation with e2 elements 
        """

        activity_durations = bpmn_e2_diagram.activity_durations
        monitoring_groups = bpmn_e2_diagram.monitoring_groups
        activity_effects = bpmn_e2_diagram.activity_effects
        decision_points = bpmn_e2_diagram.decision_points
        associations = bpmn_e2_diagram.associations
        
        document = BpmnE2DiagramGraphImport.read_xml_file(filepath)
        extension_elements = document.getElementsByTagNameNS('*', 'extensionElements')[0]

        BpmnE2DiagramGraphImport.import_activity_durations(extension_elements, activity_durations)
        BpmnE2DiagramGraphImport.import_associations(extension_elements, associations)

    @staticmethod
    def import_distribution_params(time_expected_dict, id, params) :
    
        for param in params: 
            name = param.getAttribute('name')
            value = param.getAttribute('value')
            unit = param.getAttribute('unit')

            time_expected_dict[id]['params'][name] = {
                'value': value,
                'unit': unit
            }


    @staticmethod
    def import_activity_durations(extension_elements, activity_durations):
        time_expected_xml = extension_elements.getElementsByTagNameNS('*', 'timeExpected')
        time_expected_dict = {}
        
        for time_expected in time_expected_xml:
            id = time_expected.getAttribute('id')
            description = time_expected.getAttribute('description')
            distribution = time_expected.getAttribute('probabilisticDistribution')
            params = time_expected.getElementsByTagNameNS('*', 'param')

            time_expected_dict[id] = {
                'description': description, 
                'distribution': distribution,
                'params': {}
            }

            BpmnE2DiagramGraphImport.import_distribution_params(time_expected_dict, id, params)
            
        for key in time_expected_dict.keys():
            activity_durations[key] = time_expected_dict[key]

    

    @staticmethod
    def import_associations(extension_elements, associations): 
        associations_xml = extension_elements.getElementsByTagNameNS('*', 'association')
        associations_dict = {}

        for association in associations_xml:
            id = association.getAttribute('id')
            sourceRef = association.getAttribute('sourceRef')
            targetRef = association.getAttribute('targetRef')
            direction = association.getAttribute('associationDirection')

            associations_dict[id] = {
                'sourceRef': sourceRef,
                'targetRef': targetRef,
                'associationDirection': direction
            }
            
        for key in associations_dict:
            associations[key] = associations_dict[key]


    @staticmethod
    def read_xml_file(filepath):
        """
        Reads BPMN 2.0 XML file from given filepath and returns xml.dom.xminidom.Document object.

        :param filepath: filepath of source XML file.
        """
        dom_tree = minidom.parse(filepath)
        return dom_tree
