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
        document = BpmnE2DiagramGraphImport.read_xml_file(filepath)

    @staticmethod
    def read_xml_file(filepath):
        """
        Reads BPMN 2.0 XML file from given filepath and returns xml.dom.xminidom.Document object.

        :param filepath: filepath of source XML file.
        """
        dom_tree = minidom.parse(filepath)
        return dom_tree
