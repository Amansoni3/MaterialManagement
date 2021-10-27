"""MaterialManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import EmployeView
from . import StateCityView
from . import CategoryView
from . import SubCategoryView
from . import ProductView
from . import AdminView
from . import SubCatView
from . import FinalProductView
from . import supplierView
from . import PurchaseView
from . import PurchaseDrop
from . import IssueView
from . import EmployeLoginView


urlpatterns = [
    path('admin/', admin.site.urls),

    #Employee urls

    path('employeinterface/',EmployeView.EmployeInterface),
    path('submitrecord',EmployeView.SubmitRecord),
    path('displayall/',EmployeView.DisplayAll),
    path('displayemployebyid/',EmployeView.Displayemployebyid),
    path('EditDeleteRecord/',EmployeView.EditDeleteRecord),
    path('editemployepicture/',EmployeView.EditEmployePicture),
    path('saveemployepicture',EmployeView.SaveEmployeeImage),


    #city and state url

    path('fetchallstates/',StateCityView.FetchAllStates),
    path('fetchallcities/',StateCityView.FetchAllCities),

    #CategoriesInterface

    path('categoryinterface/',CategoryView.CategoryInterface),
    path('SubmitCategory',CategoryView.SubmitCategory),
    path('displaycategory/',CategoryView.DisplayCategory),
    path('getcategoryjson/',CategoryView.GetCategoryJason),
    path('DisplayCategoryById/',CategoryView.DisplayCategoryById),
    path('EditDeleteCategory/',CategoryView.EditDeleteCategory),
    path('editcategoryimage/',CategoryView.EditCategoryImages),
    path('savecategoryimage',CategoryView.SaveCategoryImage),

    #Subcategory

    path('subcategoryinterface/',SubCategoryView.SubCategoryInterface),
    path('SubSubmitCategory',SubCategoryView.SubSubmitCategory),
    path('displaysubcategory/',SubCategoryView.DisplaySubCategory),
    path('displaysubcategorybyid/',SubCategoryView.displaysubcategorybyid),
    path('EditDeleteSubCategory/',SubCategoryView.EditDeleteSubCategory),
    path('editsubcategoryimage/',SubCategoryView.EditSubCategoryImages),
    path('savesubcategoryimage',SubCategoryView.SaveSubCategoryImage),

    #ProductInterface

    path('productinterface/',ProductView.ProductInterface),
    path('SubmitProduct',ProductView.SubmitProduct),
    path('displayproduct/',ProductView.DisplayProduct),
    path('displayproductbyid/',ProductView.displayproductbyid),
    path('EditDeleteProduct/',ProductView.EditDeleteProduct),
    path('editproductimages/',ProductView.EditProductImages),
    path('saveproductimages',ProductView.SaveProductImage),

    #CategorySubcategoryView
    path('fetchcategory/',SubCatView.FetchAllCategory),
    path('fetchsubcategory/',SubCatView.FetchAllSubcategory),

    #FinalProductView

    path('finalproduct/',FinalProductView.FinalProductInterface),
    path('fetchsizeunit/',FinalProductView.FetchAllSizeUnit),
    path('fetchweightunit/',FinalProductView.FetchAllWeightUnit),
    path('fetchfinalcagteory/',FinalProductView.FetchFinalCategory),
    path('fetchfinalsubcategory/',FinalProductView.FetchFinalSubcategory),
    path('fetchfinalproduct/',FinalProductView.FetchFinalProduct),
    path('submitfinalproduct',FinalProductView.SubmitFinalProduct),
    path('editdeletefinalrecord/',FinalProductView.EditDeleteFinalRecord),

    path('displayfinalproduct/',FinalProductView.DisplayFinalProduct),
    path('savefinalimage',FinalProductView.SaveFinalImage),

    #Supplier

    path('supplierinterface/',supplierView.SupplierInterface),
    path('submitsupplierrecord/',supplierView.SubmitSupplierRecord),
    path('displayallsupplier/',supplierView.DisplayAllSupplier),
    path('fetchsupplierjason/',supplierView.FetchSupplierJason),


    #Purchase

    path('purchaseinterface/',PurchaseView.PurchaseInterface),
    path('submitpurchaserecord/',PurchaseView.SubmitPurchaseRecord),
    path('displaypurchaseproduct/',PurchaseView.DisplayPurchaseProduct),
    path('editdeletepurchaserecord/',PurchaseView.EditDeletePurchaseRecord),

    #PurchaseJason

    path('fetchpurchasecategory/', PurchaseDrop.FetchPurchaseCategory),
    path('fetchpurchasesubcategory/', PurchaseDrop.FetchPurchaseSubcategory),
    path('fetchpurchaseproduct/', PurchaseDrop.FetchPurchaseProduct),
    path('fetchpurchasefinalproduct/', PurchaseDrop.FetchPurchaseFinalProduct),
    path('displaypurchaseproduct/',PurchaseView.DisplayPurchaseProduct),

    #AdminLogin

    path('adminlogin/',AdminView.AdminLogin),
    path('checkadminlogin',AdminView.CheckAdminLogin),

    #Dashboard

    path('admindashboard/',AdminView.AdminDashboard),
    path('adminlogout/',AdminView.AdminLogout),

    #Issue

    path('issueinterface/',IssueView.IssueInterface),
    path('submitissuerecord/',IssueView.SubmitIssueRecord),
    path('displayallissue/',IssueView.DisplayAllIssue),



    #IssueJason

    path('fetchissuecategory/',IssueView.FetchIssueCategory),
    path('fetchissuesubcategory/',IssueView.FetchIssueSubcategory),
    path('fetchissueproduct/',IssueView.FetchIssueProduct),
    path('fetchissuefinalproduct/',IssueView.FetchIssueFinalProduct),
    path('fetchallemployejason/',IssueView.FetchAllEmployeJSON),

    #EmployeeLogin

    path('employeelogin/',EmployeLoginView.EmployeeLogin),
    path('employeelogout/',EmployeLoginView.EmployeLogout),
    path('checkemployelogin',EmployeLoginView.CheckEmployeLogin),
    path('employeedashboard/',EmployeLoginView.EmployeDashboard),
    path('displayproductemploye/',EmployeLoginView.DisplayProductEmployeLogin),
    path('displayfinalproductemploye/',EmployeLoginView.DisplayFinalProductEmploye),

    #updateStock
    path('getfinalproductstockjason/',FinalProductView.GetFinalProductStockJason),





]
