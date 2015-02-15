# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.db.models.query import RawQuerySet, QuerySet


class CParameter(models.Model):
    param_uri = models.CharField(primary_key=True, max_length=80)
    param_value = models.CharField(max_length=500, blank=True)
    default_value = models.CharField(max_length=500, blank=True)
    type = models.IntegerField(blank=True, null=True)
    param_description = models.CharField(max_length=120, blank=True)
    reboot = models.CharField(max_length=1, blank=True)
    domain = models.CharField(max_length=40, blank=True)
    param_name = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'c_parameter'


class CParameterType(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'c_parameter_type'


class DDatasource(models.Model):
    datasource_name = models.CharField(primary_key=True, max_length=16)
    datasource_description = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'd_datasource'


class DEntityManager(models.Model):
    entity_manager_name = models.CharField(primary_key=True, max_length=16)
    entity_manager_description = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'd_entity_manager'


# class DismissReportIdSeq(models.Model):
#     id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dismiss_report_id_seq'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EAttachment(models.Model):
    attachment_id = models.IntegerField(primary_key=True)
    mail = models.ForeignKey('EMail')
    file_path = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'e_attachment'


class EMail(models.Model):
    mail_id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=80, blank=True)
    to_recipients = models.CharField(max_length=400)
    cc_recipients = models.CharField(max_length=400, blank=True)
    ccn_recipients = models.CharField(max_length=400, blank=True)
    message_body_text = models.CharField(max_length=4000, blank=True)
    mail_status = models.CharField(max_length=40, blank=True)
    inserted_on = models.DateTimeField(blank=True, null=True)
    sent_on = models.DateTimeField(blank=True, null=True)
    send_after = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_mail'


class EMailTemplate(models.Model):
    template_uri = models.CharField(primary_key=True, max_length=80)
    subject = models.CharField(max_length=80, blank=True)
    def_to_recipient = models.CharField(max_length=400, blank=True)
    def_cc_recipient = models.CharField(max_length=400, blank=True)
    def_ccn_recipient = models.CharField(max_length=400, blank=True)
    message_body_text = models.CharField(max_length=4000, blank=True)
    template_name = models.CharField(max_length=40, blank=True)
    template_description = models.CharField(max_length=80, blank=True)

    class Meta:
        managed = False
        db_table = 'e_mail_template'


class IDictionary(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sic = models.CharField(max_length=60)
    lang = models.ForeignKey('ILanguage')
    message = models.CharField(max_length=400, blank=True)
    domain = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'i_dictionary'


class ILanguage(models.Model):
    lang_id = models.CharField(primary_key=True, max_length=2)
    lang_name = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'i_language'


class LMessage(models.Model):
    message_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, blank=True)
    message = models.CharField(max_length=4000, blank=True)
    username = models.CharField(max_length=80, blank=True)
    message_date = models.DateTimeField(blank=True, null=True)
    message_type = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'l_message'


class MCombo(models.Model):
    combo_name = models.CharField(primary_key=True, max_length=40)
    key_name = models.CharField(max_length=40, blank=True)
    value_name = models.CharField(max_length=40, blank=True)
    datasource = models.CharField(max_length=40, blank=True)
    query = models.CharField(max_length=1000, blank=True)
    entity_manager = models.CharField(max_length=40, blank=True)
    class_name = models.CharField(max_length=100, blank=True)
    value_list = models.CharField(max_length=2000, blank=True)
    multi_select = models.CharField(max_length=1, blank=True)
    domain = models.CharField(max_length=40, blank=True)
    connected_combo = models.CharField(max_length=40, blank=True)
    filter = models.CharField(max_length=100, blank=True)
    object_status = models.CharField(max_length=40, blank=True)
    filter_fields = models.CharField(max_length=80, blank=True)

    class Meta:
        managed = False
        db_table = 'm_combo'


class MDatagrid(models.Model):
    datagrid_name = models.CharField(primary_key=True, max_length=40)
    description = models.CharField(max_length=80, blank=True)
    query = models.CharField(max_length=4000, blank=True)
    datasource = models.CharField(max_length=40)
    domain = models.CharField(max_length=40, blank=True)
    object_name = models.CharField(max_length=40, blank=True)
    filter_criteria = models.CharField(max_length=5, blank=True)
    time_in_export = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'm_datagrid'


class MDatagridDataType(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'm_datagrid_data_type'


class MDatagridField(models.Model):
    datagrid_name = models.ForeignKey(MDatagrid, db_column='datagrid_name')
    field_name = models.CharField(max_length=32)
    field_type = models.IntegerField()
    field_caption = models.CharField(max_length=40, blank=True)
    field_sic = models.CharField(max_length=40, blank=True)
    privilege = models.CharField(max_length=80, blank=True)
    visible = models.CharField(max_length=1, blank=True)
    presentation_index = models.IntegerField()
    pk_flag = models.CharField(max_length=1, blank=True, db_column="pk")
    format = models.CharField(max_length=40, blank=True)
    default_width = models.IntegerField()
    domain = models.CharField(max_length=40, blank=True)
    sortable = models.CharField(max_length=1, blank=True)
    filterable = models.CharField(max_length=1, blank=True)
    renderer = models.CharField(max_length=1000, blank=True)
    exportable = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'm_datagrid_field'


class MForm(models.Model):
    form_name = models.CharField(primary_key=True, max_length=40)
    form_description = models.CharField(max_length=80, blank=True)
    manager_class = models.CharField(max_length=60, blank=True)
    entity_manager = models.CharField(max_length=40)
    class_name = models.CharField(max_length=100, blank=True)
    view_privilege = models.CharField(max_length=80, blank=True)
    edit_privilege = models.CharField(max_length=80, blank=True)
    insert_privilege = models.CharField(max_length=80, blank=True)
    delete_privilege = models.CharField(max_length=80, blank=True)
    pk_class = models.CharField(max_length=100, blank=True)
    pk_name = models.CharField(max_length=40)
    domain = models.CharField(max_length=40, blank=True)
    columns = models.IntegerField(blank=True, null=True)
    form_type = models.CharField(max_length=8, blank=True)
    object_name = models.CharField(max_length=40, blank=True)
    before_insert = models.CharField(max_length=1000, blank=True)
    after_insert = models.CharField(max_length=1000, blank=True)
    before_edit = models.CharField(max_length=1000, blank=True)
    after_edit = models.CharField(max_length=1000, blank=True)
    before_delete = models.CharField(max_length=1000, blank=True)
    after_delete = models.CharField(max_length=1000, blank=True)
    form_layout = models.IntegerField(blank=True, null=True)
    tabs = models.CharField(max_length=800, blank=True)

    class Meta:
        managed = False
        db_table = 'm_form'


class MFormButton(models.Model):
    button_name = models.CharField(max_length=40)
    form_name = models.ForeignKey(MForm, db_column='form_name')
    button_label = models.CharField(max_length=40, blank=True)
    action = models.CharField(max_length=40, blank=True)
    form_bind = models.CharField(max_length=1, blank=True)
    script = models.CharField(max_length=4000, blank=True)
    presentation_index = models.IntegerField(blank=True, null=True)
    button_sic = models.CharField(max_length=40, blank=True)
    form_action = models.CharField(max_length=40, blank=True)
    callback_action = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'm_form_button'


class MFormDataType(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'm_form_data_type'


class MFormField(models.Model):
    form_name = models.ForeignKey(MForm, db_column='form_name')
    field_name = models.CharField(max_length=72)
    field_description = models.CharField(max_length=80, blank=True)
    field_caption = models.CharField(max_length=40, blank=True)
    field_sic = models.CharField(max_length=40, blank=True)
    mandatory = models.CharField(max_length=1, blank=True)
    field_type = models.IntegerField()
    form_field_type = models.IntegerField()
    min_length = models.IntegerField(blank=True, null=True)
    max_length = models.IntegerField(blank=True, null=True)
    pk_flag = models.CharField(max_length=1, blank=True, db_column="pk")
    presentation_index = models.IntegerField(blank=True, null=True)
    visible = models.CharField(max_length=1, blank=True)
    read_only = models.CharField(max_length=1, blank=True)
    update_privilege = models.CharField(max_length=80, blank=True)
    view_privilege = models.CharField(max_length=80, blank=True)
    combo_name = models.CharField(max_length=40, blank=True)
    virtual = models.CharField(max_length=1, blank=True)
    domain = models.CharField(max_length=40, blank=True)
    copy_value_from = models.CharField(max_length=120, blank=True)
    field_mapping = models.CharField(max_length=40, blank=True)
    script = models.CharField(max_length=4000, blank=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    on_change = models.CharField(max_length=4000, blank=True)
    filter_operator = models.CharField(max_length=8, blank=True)
    nested_property = models.CharField(max_length=80, blank=True)
    min_val = models.IntegerField(blank=True, null=True)
    max_val = models.IntegerField(blank=True, null=True)
    pos_x = models.IntegerField(blank=True, null=True)
    pos_y = models.IntegerField(blank=True, null=True)
    radio_button_name = models.CharField(max_length=40, blank=True)
    xtype_class = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'm_form_field'


class MFormFieldType(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'm_form_field_type'


class MFormLayout(models.Model):
    layout_id = models.IntegerField()
    layout_descr = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'm_form_layout'


class MMapDatastoreType(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'm_map_datastore_type'


class MMapLayer(models.Model):
    layer_name = models.CharField(primary_key=True, max_length=40)
    layer_type = models.CharField(max_length=40, blank=True)
    description = models.CharField(max_length=80, blank=True)
    points_datastore_type = models.CharField(max_length=40, blank=True)
    query_ds = models.CharField(max_length=4000, blank=True)
    manager_ds = models.CharField(max_length=100, blank=True)
    point_style = models.CharField(max_length=40, blank=True)
    point_type_name = models.CharField(max_length=80, blank=True)
    datasource = models.CharField(max_length=40)
    domain = models.CharField(max_length=40, blank=True)
    filter_criteria = models.CharField(max_length=20, blank=True)
    file_ds = models.CharField(max_length=1000, blank=True)

    class Meta:
        managed = False
        db_table = 'm_map_layer'


class MMapLayerType(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'm_map_layer_type'


class MMapPointStyle(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    description = models.CharField(max_length=100, blank=True)
    uri = models.CharField(max_length=1000, blank=True)

    class Meta:
        managed = False
        db_table = 'm_map_point_style'


class MMenu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    menu_bar = models.ForeignKey('MMenuBar', blank=True, null=True)
    menu_name = models.CharField(max_length=40, blank=True)
    menu_sic = models.CharField(max_length=60, blank=True)
    menu_description = models.CharField(max_length=80, blank=True)
    privilege = models.CharField(max_length=40, blank=True)
    presentation_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_menu'


class MMenuBar(models.Model):
    menu_bar_id = models.IntegerField(primary_key=True)
    menu_bar_name = models.CharField(max_length=40, blank=True)
    menu_bar_description = models.CharField(max_length=80, blank=True)

    class Meta:
        managed = False
        db_table = 'm_menu_bar'


class MMenuItem(models.Model):
    menu_item_id = models.IntegerField(primary_key=True)
    menu = models.ForeignKey(MMenu, blank=True, null=True)
    item_name = models.CharField(max_length=40, blank=True)
    item_sic = models.CharField(max_length=60, blank=True)
    url = models.CharField(max_length=250, blank=True)
    privilege = models.CharField(max_length=40, blank=True)
    icon = models.CharField(max_length=250, blank=True)
    presentation_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_menu_item'


class MStartMenu(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    icon = models.CharField(max_length=40, blank=True)
    icon_cls = models.CharField(max_length=40, blank=True)
    url = models.CharField(max_length=128)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    maximized = models.CharField(max_length=1, blank=True)
    privilege = models.CharField(max_length=40, blank=True)
    desktop_shortcut = models.CharField(max_length=1, blank=True)
    start_on_startup = models.CharField(max_length=1, blank=True)
    presentation_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_start_menu'


class OAttachment(models.Model):
    attachment_id = models.IntegerField(primary_key=True)
    object_name = models.CharField(max_length=40, blank=True)
    object_id = models.CharField(max_length=40, blank=True)
    userid = models.CharField(max_length=40, blank=True)
    upload_date = models.DateTimeField(blank=True, null=True)
    file_name = models.CharField(max_length=80, blank=True)
    file_size = models.IntegerField(blank=True, null=True)
    content_type = models.CharField(max_length=40, blank=True)
    note = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=80, blank=True)
    file = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'o_attachment'


class RChart(models.Model):
    chart_name = models.CharField(primary_key=True, max_length=40)
    chart_description = models.CharField(max_length=80, blank=True)

    class Meta:
        managed = False
        db_table = 'r_chart'


class RChartSerie(models.Model):
    chart_name = models.ForeignKey(RChart, db_column='chart_name')
    chart_serie = models.CharField(max_length=40)
    query = models.CharField(max_length=1000, blank=True)
    x_column = models.CharField(max_length=32, blank=True)
    y_column = models.CharField(max_length=32, blank=True)
    type = models.CharField(max_length=40, blank=True)
    display_name = models.CharField(max_length=40, blank=True)
    display_sic = models.CharField(max_length=40, blank=True)
    data_source = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'r_chart_serie'


class RReport(models.Model):
    report_id = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=40, blank=True)
    uri = models.CharField(max_length=40, blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    result_code = models.CharField(max_length=2, blank=True)
    result_message = models.CharField(max_length=80, blank=True)
    report_status = models.CharField(max_length=10, blank=True)
    file_path = models.CharField(max_length=200, blank=True)
    file_name = models.CharField(max_length=40, blank=True)
    file_format = models.CharField(max_length=4, blank=True)

    class Meta:
        managed = False
        db_table = 'r_report'


class RReportConfig(models.Model):
    uri = models.CharField(primary_key=True, max_length=80)
    report_name = models.CharField(max_length=40, blank=True)
    report_description = models.CharField(max_length=80, blank=True)
    jrxml = models.CharField(max_length=80, blank=True)
    privilege = models.CharField(max_length=80, blank=True)
    form_name = models.CharField(max_length=40, blank=True)
    data_source = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'r_report_config'


class SJob(models.Model):
    job_name = models.CharField(primary_key=True, max_length=40)
    class_name = models.CharField(max_length=100, blank=True)
    job_group_name = models.CharField(max_length=40, blank=True)
    job_description = models.CharField(max_length=80, blank=True)
    job_parameters = models.CharField(max_length=1000, blank=True)

    class Meta:
        managed = False
        db_table = 's_job'


class SJobGroup(models.Model):
    job_group_name = models.CharField(primary_key=True, max_length=40)
    job_group_description = models.CharField(max_length=80, blank=True)

    class Meta:
        managed = False
        db_table = 's_job_group'


class SJobLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    job_name = models.CharField(max_length=40, blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    result_code = models.CharField(max_length=2, blank=True)
    result_message = models.CharField(max_length=400, blank=True)
    execution_log = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 's_job_log'


class SScheduler(models.Model):
    scheduler_name = models.CharField(primary_key=True, max_length=40)
    scheduler_description = models.CharField(max_length=80, blank=True)

    class Meta:
        managed = False
        db_table = 's_scheduler'


class STriggerGroup(models.Model):
    trigger_group_name = models.CharField(primary_key=True, max_length=40)
    trigger_group_description = models.CharField(max_length=80, blank=True)

    class Meta:
        managed = False
        db_table = 's_trigger_group'


class SerialNumber(models.Model):
    id_serial = models.IntegerField(primary_key=True)
    id_operation = models.IntegerField(blank=True, null=True)
    code_operation = models.CharField(max_length=45, blank=True)
    value = models.CharField(max_length=45, blank=True)
    id_partition_name = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'serial_number'


class TPerformanceTest(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    dummy_data = models.CharField(max_length=1000, blank=True)

    class Meta:
        managed = False
        db_table = 't_performance_test'


class UAccessLog(models.Model):
    log_id = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=40, blank=True)
    remote_host = models.CharField(max_length=250, blank=True)
    log_date = models.DateTimeField(blank=True, null=True)
    success = models.CharField(max_length=1, blank=True)
    access_type = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'u_access_log'


class UArea(models.Model):
    area_name = models.CharField(primary_key=True, max_length=40)
    area_description = models.CharField(max_length=80, blank=True)

    def __unicode__(self):
        return self.area_name

    class Meta:
        managed = False
        db_table = 'u_area'


class UFunction(models.Model):
    function_name = models.CharField(primary_key=True, max_length=40)
    function_description = models.CharField(max_length=80, blank=True)

    class Meta:
        managed = False
        db_table = 'u_function'


class UPasswd(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    passwd = models.CharField(max_length=80, blank=True)
    userid = models.CharField(max_length=40, blank=True)
    flg_mobile = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'u_passwd'


class UPrivilege(models.Model):
    privilege_name = models.CharField(primary_key=True, max_length=40)
    privilege_description = models.CharField(max_length=80, blank=True)
    hidden = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'u_privilege'


class URole(models.Model):
    role_name = models.CharField(primary_key=True, max_length=40)
    role_description = models.CharField(max_length=80, blank=True)

    class Meta:
        managed = False
        db_table = 'u_role'


class URolePrivilege(models.Model):
    role_name = models.ForeignKey(URole, db_column='role_name')
    privilege_name = models.ForeignKey(UPrivilege, db_column='privilege_name')

    class Meta:
        managed = False
        db_table = 'u_role_privilege'


class UUser(models.Model):
    userid = models.CharField(primary_key=True, max_length=40)
    passwd = models.CharField(max_length=80)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    title = models.CharField(max_length=40, blank=True)
    office = models.CharField(max_length=40, blank=True)
    department = models.CharField(max_length=40, blank=True)
    locked = models.CharField(max_length=1, blank=True)
    created = models.DateField(blank=True, null=True)
    valid_from = models.DateField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    attempts_failed = models.IntegerField(blank=True, null=True)
    last_attempt_failed = models.DateTimeField(blank=True, null=True)
    password_expiration = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=80, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    mobile_phone_number = models.CharField(max_length=20, blank=True)
    notes = models.CharField(max_length=400, blank=True)
    lang_id = models.CharField(max_length=2, blank=True)
    web_user = models.CharField(max_length=2, blank=True)
    mobile_user = models.CharField(max_length=2, blank=True)
    personal_depot = models.CharField(max_length=20, blank=True)
    m_valid_from = models.DateField(blank=True, null=True)
    m_valid_to = models.DateField(blank=True, null=True)
    m_locked = models.CharField(max_length=1, blank=True)
    m_attempts_failed = models.IntegerField(blank=True, null=True)
    m_last_attempt_failed = models.DateTimeField(blank=True, null=True)
    m_passwd = models.CharField(max_length=80, blank=True)
    m_password_expiration = models.DateField(blank=True, null=True)
    last_login_mobile = models.DateTimeField(blank=True, null=True)
    country_code = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'u_user'

    def __unicode__(self):
        return self.userid





class UUserFunction(models.Model):
    userid = models.ForeignKey(UUser, db_column='userid')
    function_name = models.ForeignKey(UFunction, db_column='function_name')

    class Meta:
        managed = False
        db_table = 'u_user_function'


class UUserRole(models.Model):
    userid = models.ForeignKey(UUser, db_column='userid')
    role_name = models.ForeignKey(URole, db_column='role_name')

    class Meta:
        managed = False
        db_table = 'u_user_role'


class VTransitionLog(models.Model):
    transition_log_id = models.IntegerField()
    object_name = models.IntegerField()
    object_id = models.IntegerField()
    userid = models.IntegerField()
    transition_date = models.IntegerField()
    prev_status = models.IntegerField()
    next_status = models.IntegerField()
    username = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'v_transition_log'


class WfEvent(models.Model):
    event_name = models.CharField(primary_key=True, max_length=40)
    event_description = models.CharField(max_length=80, blank=True)

    class Meta:
        managed = False
        db_table = 'wf_event'


class WfEventListener(models.Model):
    event_name = models.ForeignKey(WfEvent, db_column='event_name')
    listener_name = models.ForeignKey('WfListener', db_column='listener_name')

    class Meta:
        managed = False
        db_table = 'wf_event_listener'


class WfEventLog(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.ForeignKey(WfEvent, db_column='event_name', blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    userid = models.ForeignKey(UUser, db_column='userid', blank=True, null=True)
    event_status = models.CharField(max_length=10, blank=True)
    processed_on = models.DateTimeField(blank=True, null=True)
    result_code = models.CharField(max_length=10, blank=True)
    result_message = models.CharField(max_length=80, blank=True)
    event_context = models.CharField(max_length=4000, blank=True)
    event_data = models.CharField(max_length=4000, blank=True)

    class Meta:
        managed = False
        db_table = 'wf_event_log'


class WfEventQueue(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.ForeignKey(WfEvent, db_column='event_name', blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    userid = models.ForeignKey(UUser, db_column='userid', blank=True, null=True)
    event_status = models.CharField(max_length=10, blank=True)
    processed_on = models.DateTimeField(blank=True, null=True)
    result_code = models.CharField(max_length=10, blank=True)
    result_message = models.CharField(max_length=80, blank=True)
    event_context = models.CharField(max_length=4000, blank=True)
    event_data = models.CharField(max_length=4000, blank=True)

    class Meta:
        managed = False
        db_table = 'wf_event_queue'


class WfListener(models.Model):
    listener_name = models.CharField(primary_key=True, max_length=40)
    listener_description = models.CharField(max_length=80, blank=True)
    listener_class = models.CharField(max_length=80, blank=True)
    status_id = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'wf_listener'


class WfObject(models.Model):
    object_name = models.CharField(primary_key=True, max_length=40)
    table_name = models.CharField(max_length=40, blank=True)
    datasource = models.CharField(max_length=40, blank=True)
    pk_fields = models.CharField(max_length=200, blank=True)
    status_field = models.CharField(max_length=40, blank=True)
    area_field = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'wf_object'


class WfObjectStatus(models.Model):
    object_name = models.ForeignKey(WfObject, db_column='object_name')
    status_name = models.CharField(max_length=40, blank=True)
    status_id = models.CharField(max_length=40)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wf_object_status'


class WfRecVisibilityFunct(models.Model):
    rule_id = models.IntegerField(primary_key=True)
    object_name = models.ForeignKey(WfObject, db_column='object_name', blank=True, null=True)
    status_id = models.CharField(max_length=40, blank=True)
    function_name = models.ForeignKey(UFunction, db_column='function_name', blank=True, null=True)
    rules = models.CharField(max_length=1000, blank=True)

    class Meta:
        managed = False
        db_table = 'wf_rec_visibility_funct'


class WfStatTransitionFunct(models.Model):
    stat_transition_funct_id = models.IntegerField(primary_key=True)
    status_transition_id = models.IntegerField(blank=True, null=True)
    function_name = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'wf_stat_transition_funct'


class WfStatusTransition(models.Model):
    status_transition_id = models.IntegerField(primary_key=True)
    object_name = models.ForeignKey(WfObject, db_column='object_name', blank=True, null=True)
    prev_status = models.CharField(max_length=40, blank=True)
    next_status = models.CharField(max_length=40, blank=True)
    pre_transition_expression = models.CharField(max_length=4000, blank=True)
    transition_validation = models.CharField(max_length=4000, blank=True)
    post_transition_expression = models.CharField(max_length=4000, blank=True)
    published_event = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'wf_status_transition'


class WfTransitionLog(models.Model):
    transition_log_id = models.IntegerField(primary_key=True)
    object_name = models.CharField(max_length=40, blank=True)
    object_id = models.CharField(max_length=40, blank=True)
    userid = models.CharField(max_length=40, blank=True)
    transition_date = models.DateTimeField(blank=True, null=True)
    prev_status = models.CharField(max_length=40, blank=True)
    next_status = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'wf_transition_log'


######################
# VIEWS #
####################

class IDictionaryLanguageView(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sic = models.CharField(max_length=60)
    message = models.CharField(max_length=400, blank=True)
    domain = models.CharField(max_length=20, blank=True)

    lang_id = models.IntegerField()
    lang_name = models.CharField(max_length=40, blank=True)

    def __unicode__(self):
        return u"sic:{0}, mex:{1}, lang:{2}".format(self.sic, self.message, self.lang_name)

    class Meta:
        managed = False
        db_table = 'idictlang'


##################
#
#   CUSTOM MANAGER
#
#####################

#NB: It is better to create a CUSTOM RawQuerySet providing it with all necessary methods to access the data.
# This is due to the fact that the manager simply proxy all the methods of the query set. So if you call objects.count()
# you really call QuerySet.count() in this case RawQuerySet.count which doesn't work :)

class IDictionaryLanguageRawManager(models.Manager):
    def get_queryset(self):
        return RawQuerySet("select `d`.`id` AS `id`,`d`.`sic` AS `sic`,`d`.`message` AS `message`,`d`.`domain` AS `domain`,`l`.`lang_id` AS `lang_id`,`l`.`lang_name` AS `lang_name` from (`i_dictionary` `d` join `i_language` `l`) where (`d`.`lang_id` = `l`.`lang_id`)",self.model)


class IDictionaryLanguageRaw(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sic = models.CharField(max_length=60)
    message = models.CharField(max_length=400, blank=True)
    domain = models.CharField(max_length=20, blank=True)

    lang_id = models.IntegerField()
    lang_name = models.CharField(max_length=40, blank=True)

    objects = IDictionaryLanguageRawManager()

    def __unicode__(self):
        return u"sic:{0}, mex:{1}, lang:{2}".format(self.sic, self.message, self.lang_name)

    class Meta:
        managed = False



#######################
#   SPECIAL CASE
######################

#
class UUserAreaManager(models.Manager):

    def get_queryset(self):
        return RawQuerySet("select row_count() as rowcount_id, uua.userid, uua.area_name from u_user_area uua",self.model)

    def get_uuserarea_of(self, user=None, area=None):
        pass

    def get_areas_of(self,user):
        pass

    def get_users_of(self, area):
        pass


class UUserArea(models.Model):
    rowcount_id = models.IntegerField(primary_key=True) #UUserArea.objects.raw("select row_count() AS rowcount_id, userid, area_name from u_user_area")[0]
    userid = models.ForeignKey(UUser, db_column='userid')
    area_name = models.ForeignKey(UArea, db_column='area_name')

    objects = UUserAreaManager()
    class Meta:
        managed = False
        db_table = 'u_user_area'
        unique_together = ('userid', 'area_name')

