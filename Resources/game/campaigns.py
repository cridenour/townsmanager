import os
from files import GameFiles
try:
    from lxml.etree import Element, SubElement
except ImportError:
    from xml.etree import Element, SubElement


class CampaignManager(object):
    """
    Class to handle changing and updating save game files
    """

    _files = None

    def __init__(self, files):

        if not isinstance(files, GameFiles):
            raise TypeError("Files object should be of type GameFiles")
        self._files = files
        self._c1 = None

    def getPlayerCampaign(self):
        """
        Returns a representation of the player campaign
        """

        # Get the folders from the player campaign folder
        c1_base, c1_dirs, c1_files = self._files.list_directory('data/campaigns/c1')

        # Get a list of missions from the campaigns.xml file
        campaign_xml = self._files.parse_xml('data/campaigns.xml')
        self._c1 = Campaign.createCampaignFromXML(campaign_xml.find('campaign'))

        for m in self._c1.missions:
            if m.id in c1_dirs:
                m_base, m_dirs, m_files = self._files.list_directory(os.path.join(c1_base, m.id))
                m._directory = m_base
                m._files = m_files

        return self._c1

    def setPlayerCampaign(self, campaign):
        """
        Sets the campaign object manually
        """
        self._c1 = campaign


    def createPlayerMission(self, id, name, nameES, baseType):
        """
        Will create both the mission object and the mission folder for a new mission file
        """
        m = Mission.createMissionFromDict({
            'id': id,
            'name': name,
            'nameES': nameES,
            'baseType': baseType
        })

        self._c1.missions.append(m)


        self._files.copy_folder('data/campaigns/c1/%s' % baseType, 'data/campaigns/c1/%s' % id)


    def deletePlayerMission(self, id, delete_files=True):
        """
        Will delete the mission object and mission folder if specified.
        """
        for m in self._c1.missions:
            if m.id == id:
                self._c1.missions.remove(m)

        if delete_files:
            try:
                self._files.delete_folder('data/campaigns/c1/%s' % id)
            except OSError:
                pass

    def saveToXML(self):
        """
        Save our new campaign XML file with update missions
        """
        campaign_xml = self._files.parse_xml('data/campaigns.xml')

        c1 = campaign_xml.find('campaign')
        campaign_xml.remove(c1)
        new_c1 = self._c1.campaignXMLElement()
        self._files.indent_xml(new_c1, 1)
        campaign_xml.insert(0, new_c1)

        self._files.save_xml('data/campaigns-new.xml', campaign_xml)


class Campaign(object):
    """
    Python object representing the Campaign object
    """

    def __init__(self):
        self.id = None
        self.name = None
        self.nameES = None
        self.missions = []

    @staticmethod
    def createCampaignFromXML(et_obj):
        """
        Creates the object from the XML element campaign
        """
        c = Campaign()

        c.id = et_obj.find('id').text
        c.name = et_obj.find('name').text
        c.nameES = et_obj.find('name').attrib.get('esES')

        for m in et_obj.findall('mission'):
            c.missions.append(Mission.createMissionFromXML(m))

        return c

    @staticmethod
    def createCampaignFromDict(c_obj):
        """
        Create the object from a dict representation
        """
        c = Campaign()

        c.id = c_obj.get('id')
        c.name = c_obj.get('name')
        c.nameES = c_obj.get('nameES')

        for m in c_obj.get('missions', []):
            c.missions.append(Mission.createMissionFromDict(m))

        return c

    def campaignXMLElement(self):
        """
        Return the campaign object as an XML element
        """
        c = Element('campaign')

        id = SubElement(c, 'id')
        id.text = self.id

        name = SubElement(c, 'name', {'esES': self.nameES})
        name.text = self.name

        for m in self.missions:
            c.append(m.missionXMLElement())

        return c

    def __iter__(self):
        for m in self.missions:
            yield m

    def __len__(self):
        return len(self.missions)

    def __repr__(self):
        return 'Campaign %s (id: %s, missions: %s)' % (self.name, self.id, len(self))



class Mission(object):
    """
    Python object representing individual missions
    """


    def __init__(self):
        # Base attributes
        self.id = None
        self.name = None
        self.nameES = None
        self.baseType = None

        # Private attributes used for validation
        self._directory = None
        self._files = []

    @staticmethod
    def createMissionFromXML(et_obj):
        """
        Creates the mission object from the XML element campaign
        """
        m = Mission()

        m.id = et_obj.find('id').text
        m.name = et_obj.find('name').text
        m.nameES = et_obj.find('name').attrib.get('esES')
        m.baseType = et_obj.attrib.get('baseType')

        return m

    @staticmethod
    def createMissionFromDict(m_obj):
        """
        Create the mission object from dict representation
        """
        m = Mission()

        m.id = m_obj.get('id')
        m.name = m_obj.get('name')
        m.nameES = m_obj.get('nameES')
        m.baseType = m_obj.get('baseType')

        return m

    def missionXMLElement(self):
        """
        Return the mission object as an XML element
        """
        m = Element('mission')

        # Set our base type
        if self.baseType is not None:
            m.attrib['baseType'] = self.baseType

        id = SubElement(m, 'id')
        id.text = self.id

        name = SubElement(m, 'name', {'esES': self.nameES})
        name.text = self.name

        return m

    def __repr__(self):
        return 'Mission %s (id: %s, baseType: %s)' % (self.name, self.id, self.baseType)

if __name__ == "__main__":
    files = GameFiles()
    campaignManager = CampaignManager(files)

    c1 = campaignManager.getPlayerCampaign()
    for m in c1:
        print m
