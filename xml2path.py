import os
import shutil

root_dir = "manifest-versions"
root_dir_lkgm = "manifest-versions/LKGM-candidates"
root_dir_paladin = "manifest-versions/paladin"
format = ".xml"


class manifest_versions:
    def __init__(self, xml_name):
        pass
    def update(self):
        pass

    def chDirto(self, path):
        pass

    def get_path(self, xml):
        # chDirto(root_dir)
        # update()
        return self.find(str(xml))


    def find(xml):
        for root,dirs,files in os.walk(root_dir_lkgm):
            if files:
                for file in files:
                    # print file.rstrip('.xml')
                    if file.endswith(format) and file.rstrip('.xml') == xml:
                        print(file)
                        return os.path.join(root,file)
        for root,dirs,files in os.walk(root_dir_paladin):
            if files:
                for file in files:
                    # print file.rstrip('.xml')
                    if file.endswith(format) and file.rstrip('.xml') == xml:
                        print(file)
                        return os.path.join(root,file)
        return False