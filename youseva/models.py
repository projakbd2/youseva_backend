# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AddonProduct(models.Model):
    product = models.ForeignKey('Product', models.DO_NOTHING, related_name="addon_product_product")
    addon_product_description_txt = models.CharField(max_length=500, blank=True, null=True)
    related_product = models.ForeignKey('Product', models.DO_NOTHING, related_name="addon_product_related_product")
    addon_product_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'addon_product'


class AttrGrp(models.Model):
    attribute_group_cd = models.CharField(primary_key=True, max_length=50)
    attribute_group_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attr_grp'


class Attribute(models.Model):
    attribute_id = models.IntegerField(primary_key=True)
    attribute_group_cd = models.ForeignKey(AttrGrp, models.DO_NOTHING, db_column='attribute_group_cd', blank=True, null=True, related_name="attribute_attribute_group_cd")
    attribute_name = models.CharField(max_length=50, blank=True, null=True)
    attr_notes = models.CharField(max_length=50, blank=True, null=True)
    created_ts = models.DateTimeField(blank=True, null=True)
    updated_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute'


class AttributeValueList(models.Model):
    attribute_value_id = models.IntegerField(primary_key=True)
    attribute = models.ForeignKey(Attribute, models.DO_NOTHING, related_name="attribute_valueList_attribute")
    value = models.CharField(max_length=50)
    created_ts = models.DateTimeField(blank=True, null=True)
    updated_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute_value_list'


class AttributeValueType(models.Model):
    attribute_value_type_cd = models.CharField(primary_key=True, max_length=50)
    attribute_value_type_nm = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute_value_type'


class Brand(models.Model):
    brand_id = models.IntegerField(primary_key=True)
    slug = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    logo_url = models.TextField(blank=True, null=True)
    brand_banner = models.ForeignKey('Media', models.DO_NOTHING, blank=True, null=True, related_name="brand_banner_media")
    banner_url = models.TextField(blank=True, null=True)
    created_ts = models.DateTimeField(blank=True, null=True)
    updated_ts = models.DateTimeField(blank=True, null=True)
    brand_logo = models.ForeignKey('Media', models.DO_NOTHING, blank=True, null=True, related_name="brand_logo_media")

    class Meta:
        managed = False
        db_table = 'brand'


class Checkout(models.Model):
    checkout_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    merchant_id = models.IntegerField()
    coupon_id = models.IntegerField(blank=True, null=True)
    trx_id = models.IntegerField(blank=True, null=True)
    coupon_discount_amount = models.FloatField(default=0.000)
    status = models.IntegerField(default=0)
    created_ts = models.DateTimeField(blank=True, null=True)
    updated_ts = models.DateTimeField(blank=True, null=True)
    cart_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cart_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkout'


class Currency(models.Model):
    currency_id = models.IntegerField(primary_key=True)
    currency_cd = models.CharField(max_length=10, blank=True, null=True)
    currency_name = models.CharField(max_length=100, blank=True, null=True)
    currency_symbol = models.CharField(max_length=10, blank=True, null=True)
    currency_format = models.CharField(max_length=30, blank=True, null=True, default="us")
    symbol_direction = models.CharField(max_length=30, blank=True, null=True, default="left")
    exchange_rate = models.FloatField()
    created_ts = models.DateTimeField(blank=True, null=True)
    updated_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currency'


class Feature(models.Model):
    feature_id = models.IntegerField(primary_key=True)
    feature_group_cd = models.ForeignKey('FeatureGrp', models.DO_NOTHING, db_column='feature_group_cd', blank=True, null=True, related_name="feature_feature_group_cd")
    feature_name = models.CharField(max_length=50, blank=True, null=True)
    feature_description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feature'


class FeatureGrp(models.Model):
    feature_group_cd = models.CharField(primary_key=True, max_length=50)
    feature_group_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feature_grp'


class Language(models.Model):
    language_id = models.IntegerField(primary_key=True)
    language_name = models.CharField(max_length=255)
    short_form = models.CharField(max_length=20)
    language_cd = models.CharField(max_length=20)
    text_direction = models.CharField(max_length=10)
    status = models.IntegerField(default=1)
    language_order = models.IntegerField(default=1)
    text_editor_lang = models.CharField(max_length=10, blank=True, null=True, default="en")
    flag_path = models.CharField(max_length=255, blank=True, null=True)
    locale = models.CharField(max_length=30)
    flag = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language'


class ListedPackage(models.Model):
    attribute = models.ForeignKey(Attribute, models.DO_NOTHING, related_name="listed_package_attribute")
    attribute_value = models.CharField(max_length=2500, blank=True, null=True)
    feature = models.ForeignKey(Feature, models.DO_NOTHING, related_name="listed_package_feature")
    attribute_value_type_cd = models.ForeignKey(AttributeValueType, models.DO_NOTHING, db_column='attribute_value_type_cd', related_name="listed_package_attribute_value_type_cd")
    uom_cd = models.ForeignKey('UnitOfMeasure', models.DO_NOTHING, db_column='uom_cd', related_name="listed_package_ucom_cd")
    product_package = models.ForeignKey('ProductPackage', models.DO_NOTHING, related_name="listed_package_product_package")
    attribute_value_0 = models.OneToOneField(AttributeValueList, models.DO_NOTHING, db_column='attribute_value_id', primary_key=True, related_name="attribute_value_0")  # Field renamed because of name conflict.
    created_ts = models.DateTimeField(blank=True, null=True)
    updated_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listed_package'
        unique_together = (('attribute_value_0', 'attribute', 'feature', 'uom_cd', 'attribute_value_type_cd', 'product_package'),)


class Media(models.Model):
    media_id = models.IntegerField(primary_key=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    storage = models.CharField(max_length=20, blank=True, null=True, default="local")
    name = models.CharField(max_length=250, blank=True, null=True)
    media_type_cd = models.CharField(max_length=10, blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    original_file = models.CharField(max_length=50, blank=True, null=True)
    image_variants = models.TextField(blank=True, null=True)
    created_ts = models.DateTimeField(blank=True, null=True)
    updated_ts = models.DateTimeField(blank=True, null=True)
    media_url = models.CharField(max_length=255, blank=True, null=True)
    media_owner_id = models.IntegerField(blank=True, null=True)
    media_creator_id = models.IntegerField(blank=True, null=True)
    media_language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True, related_name="media_media_language")

    class Meta:
        managed = False
        db_table = 'media'


class PackageType(models.Model):
    package_type_id = models.IntegerField(primary_key=True)
    package_type_name = models.CharField(max_length=100, blank=True, null=True)
    package_items_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_type'


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    slug = models.CharField(max_length=500, blank=True, null=True)
    listing_type = models.CharField(max_length=20, blank=True, null=True, default="sell_on_site")
    sku = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=20, blank=True, null=True)
    discount_rate = models.SmallIntegerField(blank=True, null=True, default=0)
    vat_rate = models.FloatField(blank=True, null=True, default=0)
    status = models.IntegerField(default=0)
    is_promoted = models.IntegerField(blank=True, null=True, default=0)
    promote_start_date = models.DateTimeField(blank=True, null=True)
    promote_end_date = models.DateTimeField(blank=True, null=True)
    promote_plan = models.CharField(max_length=100, blank=True, null=True)
    promote_day = models.IntegerField(blank=True, null=True)
    is_special_offer = models.IntegerField(blank=True, null=True, default=0)
    special_offer_date = models.DateTimeField(blank=True, null=True)
    visibility = models.IntegerField(default=1)
    rating = models.CharField(max_length=50, blank=True, null=True, default=0)
    pageviews = models.IntegerField(blank=True, null=True, default=0)
    demo_url = models.CharField(max_length=1000, blank=True, null=True)
    external_link = models.CharField(max_length=1000, blank=True, null=True)
    files_included = models.CharField(max_length=255, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True, default=1)
    multiple_sale = models.IntegerField(blank=True, null=True, default=1)
    soldout_ind = models.CharField(max_length=1, default=0)
    is_deleted = models.IntegerField(blank=True, null=True, default=0)
    is_draft = models.IntegerField(blank=True, null=True, default=0)
    is_free_product = models.IntegerField(blank=True, null=True, default=0)
    is_rejected = models.IntegerField(blank=True, null=True, default=0)
    reject_reason = models.CharField(max_length=1000, blank=True, null=True)
    created_ts = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    managed_product_ind = models.CharField(max_length=1)
    product_sub_category_id = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    product_type = models.ForeignKey('ProductType', models.DO_NOTHING, blank=True, null=True, related_name="product_product_type")
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True, related_name="product_brand")
    updated_ts = models.DateTimeField(blank=True, null=True)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    addon_product_ind = models.CharField(max_length=1)
    spare_part_ind = models.CharField(max_length=1)
    licence_key_value = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductCategory(models.Model):
    category_id = models.IntegerField(primary_key=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    title_meta_tag = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    keywords = models.CharField(max_length=500, blank=True, null=True)
    category_order = models.IntegerField(blank=True, null=True, default=0)
    featured_order = models.IntegerField(blank=True, null=True, default=1)
    homepage_order = models.IntegerField(blank=True, null=True, default=5)
    visibility = models.IntegerField(blank=True, null=True, default=1)
    show_on_main_menu = models.IntegerField(blank=True, null=True, default=1)
    show_image_on_main_menu = models.IntegerField(blank=True, null=True, default=0)
    show_products_on_index = models.IntegerField(blank=True, null=True, default=0)
    show_subcategory_products = models.IntegerField(blank=True, null=True, default=0)
    storage = models.CharField(max_length=20, blank=True, null=True, default="local")
    image = models.CharField(max_length=255, blank=True, null=True)
    created_ts = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    product_group = models.ForeignKey('ProductGroup', models.DO_NOTHING, blank=True, null=True, related_name="product_category_product_group")
    service_category_ind = models.CharField(max_length=1, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    commission = models.FloatField(blank=True, null=True)
    status = models.IntegerField()
    icon = models.ForeignKey(Media, models.DO_NOTHING, blank=True, null=True, related_name="product_category_icon")
    logo = models.ForeignKey(Media, models.DO_NOTHING, blank=True, null=True, related_name="product_category_logo")
    updated_ts = models.DateTimeField(blank=True, null=True)
    banner = models.ForeignKey(Media, models.DO_NOTHING, blank=True, null=True, related_name="product_category_banner")
    featured_ind = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductDigitalCatalog(models.Model):
    digital_catalog_id = models.IntegerField(primary_key=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    storage = models.CharField(max_length=20, blank=True, null=True, default="local")
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True, related_name="product_digital_catalog_product")
    user_id = models.IntegerField(blank=True, null=True)
    licence_key_value = models.CharField(max_length=100, blank=True, null=True)
    license_expiry_date = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_digital_catalog'


class ProductGroup(models.Model):
    product_group_id = models.IntegerField(primary_key=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    show_on_main_menu = models.IntegerField(blank=True, null=True)
    show_image_on_main_menu = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    created_ts = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    service_group_ind = models.CharField(max_length=1, blank=True, null=True)
    logo = models.ForeignKey(Media, models.DO_NOTHING, blank=True, null=True, related_name="product_group_logo")
    icon = models.ForeignKey(Media, models.DO_NOTHING, blank=True, null=True, related_name="product_group_icon")

    class Meta:
        managed = False
        db_table = 'product_group'


class ProductLanguage(models.Model):
    product_language_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, related_name="product_language_product_language_id")
    lang = models.CharField(max_length=10, default="en")
    name = models.CharField(max_length=50)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pdf_specification_id = models.IntegerField(blank=True, null=True)
    pdf_specification = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    meta_title = models.CharField(max_length=50, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=50, blank=True, null=True)
    created_ts = models.DateTimeField(blank=True, null=True)
    updated_ts = models.DateTimeField(blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True, related_name="product_language_language")

    class Meta:
        managed = False
        db_table = 'product_language'


class ProductMedia(models.Model):
    product_media_id = models.IntegerField(primary_key=True)
    image_default = models.CharField(max_length=255, blank=True, null=True)
    image_big = models.CharField(max_length=255, blank=True, null=True)
    image_small = models.CharField(max_length=255, blank=True, null=True)
    is_main = models.IntegerField(blank=True, null=True, default=0)
    storage = models.CharField(max_length=20, blank=True, null=True, default="local")
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True, related_name="produt_media_product")
    created_ts = models.DateTimeField(blank=True, null=True)
    updated_ts = models.DateTimeField(blank=True, null=True)
    media = models.ForeignKey(Media, models.DO_NOTHING, blank=True, null=True, related_name="product_media_media")

    class Meta:
        managed = False
        db_table = 'product_media'


class ProductPackage(models.Model):
    product_package_name = models.CharField(max_length=50, blank=True, null=True)
    product_variant_code = models.CharField(max_length=18, blank=True, null=True)
    marketplace_sku = models.IntegerField()
    product_package_id = models.IntegerField(primary_key=True)
    package_type = models.ForeignKey(PackageType, models.DO_NOTHING, blank=True, null=True, related_name="product_package_package_type")
    parent_package = models.ForeignKey(PackageType, models.DO_NOTHING, blank=True, null=True, related_name="product_package_parent_package")
    price = models.IntegerField(blank=True, null=True)
    discount_rate = models.SmallIntegerField(blank=True, null=True)
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    parent_product = models.ForeignKey(Product, models.DO_NOTHING)
    variation_type = models.CharField(max_length=50, blank=True, null=True)
    show_images_on_slider = models.IntegerField(blank=True, null=True)
    visible_ind = models.CharField(max_length=1)
    label_names = models.TextField(blank=True, null=True)
    insert_type = models.CharField(max_length=10, blank=True, null=True)
    option_display_type = models.CharField(max_length=30, blank=True, null=True)
    use_different_price = models.IntegerField(blank=True, null=True)
    created_ts = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    currency = models.ForeignKey(Currency, models.DO_NOTHING, blank=True, null=True, related_name="product_package_currency")

    class Meta:
        managed = False
        db_table = 'product_package'


class ProductSetting(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING, related_name="product_setting_product")
    marketplace_sku = models.IntegerField(default=1)
    marketplace_variations = models.IntegerField(blank=True, null=True, default=1)
    marketplace_shipping = models.IntegerField(blank=True, null=True, default=1)
    marketplace_product_location = models.IntegerField(blank=True, null=True, default=1)
    classified_price = models.IntegerField(blank=True, null=True, default=1)
    classified_price_required = models.IntegerField(blank=True, null=True, default=1)
    classified_product_location = models.IntegerField(blank=True, null=True, default=1)
    classified_external_link = models.IntegerField(blank=True, null=True, default=1)
    physical_demo_url = models.IntegerField(blank=True, null=True, default=0)
    physical_video_preview = models.IntegerField(blank=True, null=True, default=1)
    physical_audio_preview = models.IntegerField(blank=True, null=True, default=1)
    digital_demo_url = models.IntegerField(blank=True, null=True, default=1)
    digital_video_preview = models.IntegerField(blank=True, null=True, default=1)
    digital_audio_preview = models.IntegerField(blank=True, null=True, default=1)
    digital_allowed_file_extensions = models.CharField(max_length=500, blank=True, null=True, default="zip")
    sitemap_frequency = models.CharField(max_length=30, blank=True, null=True, default="monthly")
    sitemap_last_modification = models.CharField(max_length=30, blank=True, null=True, default="server_response")
    sitemap_priority = models.CharField(max_length=30, blank=True, null=True, default="automatically")
    product_tax_id = models.IntegerField()
    product_msrp_amount = models.FloatField()
    created_ts = models.DateTimeField(blank=True, null=True)
    updated_ts = models.DateTimeField(blank=True, null=True)
    lang_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    seo_title = models.CharField(max_length=500, blank=True, null=True)
    seo_description = models.CharField(max_length=500, blank=True, null=True)
    seo_keywords = models.CharField(max_length=500, blank=True, null=True)
    product_setting_it = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'product_setting'


class ProductSubCategory(models.Model):
    slug = models.CharField(max_length=255, blank=True, null=True)
    title_meta_tag = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    keywords = models.CharField(max_length=500, blank=True, null=True)
    category_order = models.IntegerField(blank=True, null=True)
    featured_order = models.IntegerField(blank=True, null=True)
    homepage_order = models.IntegerField(blank=True, null=True)
    visibility = models.IntegerField(blank=True, null=True)
    featured_ind = models.IntegerField()
    show_on_main_menu = models.IntegerField(blank=True, null=True)
    show_image_on_main_menu = models.IntegerField(blank=True, null=True)
    show_products_on_index = models.IntegerField(blank=True, null=True)
    show_subcategory_products = models.IntegerField(blank=True, null=True)
    storage = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    created_ts = models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True, related_name="product_subcategory_product_category")
    managed_sub_category_ind = models.CharField(max_length=1, blank=True, null=True)
    service_sub_category_ind = models.CharField(max_length=1, blank=True, null=True)
    banner = models.ForeignKey(Media, models.DO_NOTHING, blank=True, null=True, related_name="product_subcategory_banner")
    logo = models.ForeignKey(Media, models.DO_NOTHING, blank=True, null=True, related_name="product_subcategory_logo")
    icon = models.ForeignKey(Media, models.DO_NOTHING, blank=True, null=True, related_name="product_subcategory_icon")

    class Meta:
        managed = False
        db_table = 'product_sub_category'


class ProductTaxRate(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True, related_name="product")
    product_tax_rate_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'product_tax_rate'


class ProductType(models.Model):
    product_type_id = models.IntegerField(primary_key=True)
    product_type_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_type'


class Status(models.Model):
    status_cd = models.CharField(primary_key=True, max_length=10)
    status_name = models.CharField(max_length=100, blank=True, null=True)
    status_description_txt = models.CharField(max_length=500, blank=True, null=True)
    status_type_cd = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'


class UnitOfMeasure(models.Model):
    decimal_place_num = models.SmallIntegerField(blank=True, null=True)
    uom_cd = models.CharField(primary_key=True, max_length=10)
    uom_nm = models.CharField(max_length=100, blank=True, null=True)
    uom_type_cd = models.ForeignKey('UomType', models.DO_NOTHING, db_column='uom_type_cd', blank=True, null=True, related_name="unit_of_measure_uom_type_cd")

    class Meta:
        managed = False
        db_table = 'unit_of_measure'


class UomType(models.Model):
    uom_type_cd = models.CharField(primary_key=True, max_length=10)
    uom_type_nm = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uom_type'


class Wishlist(models.Model):
    user_id = models.IntegerField()
    product = models.ForeignKey(Product, models.DO_NOTHING, related_name="wishlist_product")
    created_ts = models.DateTimeField(blank=True, null=True)
    updated_ts = models.DateTimeField(blank=True, null=True)
    wishlist_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'wishlist'
