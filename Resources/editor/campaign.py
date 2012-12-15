import os

from game.files import GameFiles
from game.campaigns import CampaignManager, Campaign, Mission

f = GameFiles()
cm = CampaignManager(f)

def saveCampaign(c_data):
    """
    What gets sent back to Python is almost a Campaign object
    """
    new_campaign = Campaign.createCampaignFromDict(
        {
            'id': c_data.id,
            'name': c_data.name,
            'nameES': c_data.nameES,
        }
    )

    cm.setPlayerCampaign(new_campaign)

    for m in c_data.missions:
        if m.isNew:
            try:
                cm.createPlayerMission(m.id, m.name, m.nameES, m.baseType)
            except OSError:
                # Usually folder already exists. TODO: Add error message
                pass
        elif m.isDeleted:
            cm.deletePlayerMission(m.id)
        else:
            cm._c1.missions.append(Mission.createMissionFromDict({
                'id': m.id,
                'name': m.name,
                'nameES': m.nameES,
                'baseType': m.baseType
            }))

    cm.saveToXML()

    return os.path.join(cm._files.find_directory(), 'data/campaigns.xml')


window.editor.loadCampaign = lambda: cm.getPlayerCampaign()
window.editor.saveCampaign = saveCampaign