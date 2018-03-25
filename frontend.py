
from PyQt4 import QtCore, QtGui
from mainWindowUi import Ui_MainWindow
from params import widgets_dict


class Frontend(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, backend):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.backend = backend
        # params =======================================================
        self._current_selected_item = None
        # ==============================================================
        self.filter_list_listWidget.clear()
        self._enableAll(False)
        # connect signals ==============================================
        self.filter_list_listWidget.currentItemChanged.connect(self.item_changed)
        self.add_woman_pushButton.clicked.connect(self.on_add_woman)
        self.edit_woman_pushButton.clicked.connect(self.on_edit_woman)
        self.delete_woman_pushButton.clicked.connect(self.on_delete_woman)
        self.save_woman_pushButton.clicked.connect(self.on_save_woman)

        self.add_child_pushButton.clicked.connect(self.on_add_child)
        self.edit_child_pushButton.clicked.connect(self.on_edit_child)
        self.delete_child_pushButton.clicked.connect(self.on_delete_child)
        self.save_child_pushButton.clicked.connect(self.on_save_child)

        # this teo line for testing. remove the later
        self.add_item_to_list('rajab', 222)
        self.add_item_to_list('legnain', 111)

    def item_changed(self, x):
        self._current_selected_item = x
        print(self._current_selected_item.familyid)

    def on_add_woman(self):
        """ Enables and clear all widgets to add new woman entry """
        # deselect the current selected item if not none
        if self._current_selected_item:
            self.filter_list_listWidget.setItemSelected(self._current_selected_item, False)
        # set self._current_selected_item to none
        self._current_selected_item = None
        # clear all widgets
        self._clearAll()
        # enable all widgets to fill in
        self._enableAll(True)

    def on_edit_woman(self):
        # if an item is selected
        if not self._current_selected_item:
            # just enable widget to be edited
            self._enableAll(True)

    def on_delete_woman(self):
        # get selected family id
        familyid = self._current_selected_item.familyid
        # ask backend to delete the selected item
        self.backend.ask_deleteWoman(familyID=familyid)

    def on_save_woman(self):
        # get data from widget
        info_dict = self._get_woman_info()
        # ask backend to save changes
        # if new entry
        if self._current_selected_item is None:
            familyid = None
            self.backend.ask_addWoman(info_dict)
        else:
            familyid = self._current_selected_item.familyid
            self.backend.ask_change(info_dict)

    def on_add_child(self):
        pass

    def on_edit_child(self):
        pass

    def on_delete_child(self):
        pass

    def on_save_child(self):
        pass

    def _get_woman_info(self):
        """ Returns a dict that has all the values in the widgets"""
        d = dict()
        d['first name'] = self.first_name_lineEdit.text()
        d['last name'] = self.last_name_lineEdit.text()
        d['data of birth'] = self.woman_data_of_birth_dateEdit.text()
        d['study level'] = self.study_level_comboBox.currentText()
        d['address'] = self.address_lineEdit.text ()
        d['phone number'] = self.address_lineEdit.text()
        d['marital status'] = self.marital_status_comboBox.currentText()
        d['health status'] = self.health_status_lineEdit.text()
        d['income'] = self.income_lineEdit.text()
        d['occupation'] = self.occupation_lineEdit.text()
        d['need training'] = self.need_training_checkBox.isChecked()
        d['reason'] = self.reason_lineEdit.text()
        d['training'] = self.training_lineEdit.text()
        d['need transportation'] = self.need_transportation_checkBox.isChecked()
        d['available time'] = self.available_time_comboBox.currentText()

        return d

    def _get_child_info(self):
        d = dict()
        d['first name'] = self.child_first_name_lineEdit.text()
        d['last name'] = self.child_last_name_lineEdit.text()
        d['data of birth'] = self.child_data_of_birth_dateEdit.text()
        d['study level'] = self.child_study_level_comboBox.currentText()
        d['grad last year'] = self.grade_last_year_comboBox.currentText()
        d['hobbies'] = self.hobbies_lineEdit.text()
        d['need transportation'] = self.child_need_transportation_checkBox.isChecked()
        c = []
        if self.math_course_checkBox.isChecked():
            c.append('math')
        if self.english_course_checkBox.isChecked():
            c.append('english')
        if self.arabic_course_checkBox.isChecked():
            c.append('arabic')
        if self.computer_course_checkBox.isChecked():
            c.append('computer')
        if self.science_course_checkBox.isChecked():
            c.append('science')
        if self.islamic_course_checkBox.isChecked():
            c.append('islamic')
        d['courses'] = c

        return d

    def _clearAll(self):
        self.first_name_lineEdit.clear()
        self.last_name_lineEdit.clear()
        self.address_lineEdit.clear()
        self.phone_number_Edit.clear()
        self.occupation_lineEdit.clear()
        self.health_status_lineEdit.clear()
        self.income_lineEdit.clear()
        self.reason_lineEdit.clear()
        self.training_lineEdit.clear()
        self.child_first_name_lineEdit.clear()
        self.child_last_name_lineEdit.clear()
        self.children_listWidget.clear()
        self.hobbies_lineEdit.clear()

    def _enableAll(self, flag=False):
        self.main_groupBox.setEnabled(flag)

    def add_item_to_list(self, name='', familyid=None):
        # create item
        item = MyQlistItem(name, familyid)
        # add item to list
        self.filter_list_listWidget.addItem(item)


    def ask_update(self, d):
        """ Updates widget value """
        self.first_name_lineEdit.setText(d['first name'])
        self.last_name_lineEdit.setText(d['last name'])
        print(d['data of birth'])
        self.woman_data_of_birth_dateEdit.setDate(d['data of birth'])
        self.study_level_comboBox.setCurrentIndex(self.study_level_comboBox.findText(d['study level']))
        self.address_lineEdit.setText(d['address'])
        self.address_lineEdit.setText(d['phone number'])
        self.marital_status_comboBox.setCurrentIndex(self.marital_status_comboBox.findText(d['marital status']))
        self.health_status_lineEdit.setText(d['health status'])
        self.income_lineEdit.setText(d['income'])
        self.occupation_lineEdit.setText(d['occupation'])
        self.need_training_checkBox.setChecked(d['need training'])
        self.reason_lineEdit.setText(d['reason'])
        self.training_lineEdit.setText(d['training'])
        self.need_transportation_checkBox.setChecked(d['need transportation'])
        self.available_time_comboBox.setCurrentIndex(self.available_time_comboBox.findText(d['available time']))
        # update children
        # <>

class MyQlistItem(QtGui.QListWidgetItem ):

    def __init__(self, name='', familyid=None):
        QtGui.QListWidgetItem .__init__(self, name)
        self.familyid = familyid



if __name__ == "__main__":
    import sys
    a = QtGui.QApplication(sys.argv)
    d = dict()
    d['family id'] = 1
    d['first name'] = 'Mona'
    d['last name'] = 'Ahmed'
    d['data of birth'] = QtCore.QDate.fromString("20200110", "yyyyMMdd") #QtCore.QDate.currentDate()
    d['address'] = ''
    d['phone number'] = '612-22-222'

    w = Frontend(None)
    w.ask_update(d)
    w.show()
    a.exec_()
