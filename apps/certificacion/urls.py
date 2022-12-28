# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.certificacion.views import * 
from apps.certificacion.render_to_pdf import *
from apps.certificacion.sincronizar import *


urlpatterns = [

    path('asesorador/list/', AsesoradorListView.as_view(), name='asesorador_list'),
    path('asesorador/create/', AsesoradorCreateView.as_view(), name='asesorador_create'),
    path('asesorador/<int:pk>/update/', AsesoradorUpdateView.as_view(), name='asesorador_update'),
    path('asesorador/<int:pk>/delete/', AsesoradorDeleteView.as_view(), name='asesorador_delete'),
    #path('asesorador/<int:pk>/details/', AsesoradorDetailView.as_view(), name='asesorador_detail'),

    path('certificador/list/',CertificadorListView.as_view(), name='certificador_list'),
    path('certificador/create/', CertificadorCreateView.as_view(), name='certificador_create'),
    path('certificador/<int:pk>/update/', CertificadorUpdateView.as_view(), name='certificador_update'),
    path('certificador/<int:pk>/delete/', CertificadorDeleteView.as_view(), name='certificador_delete'),
    #path('certificador/<int:pk>/details/', CertificadorDetailView.as_view(), name='certificador_detail'),


    path('cliente/list/',ClienteListView.as_view(), name='cliente_list'),
    path('cliente/sincronizar/',ConSQL.as_view(), name='cliente_sincronizar'),
    path('cliente/create/', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/<str:pk>/update/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/<str:pk>/delete/', ClienteDeleteView.as_view(), name='cliente_delete'),
    #path('cliente/<int:pk>/details/', ClienteDetailView.as_view(), name='cliente_detail'),


    path('psi/list/',PsiListView.as_view(), name='psi_list'),
    path('psi/create/', PsiCreateView.as_view(), name='psi_create'),
    path('psi/<int:pk>/update/', PsiUpdateView.as_view(), name='psi_update'),
    path('psi/<int:pk>/delete/', PsiDeleteView.as_view(), name='psi_delete'),
    #spath('psi/<int:pk>/details/', PsiDetailView.as_view(), name='psi_detail'),
    
    
    path('certifico/pendiente/list/',CertificoPendienteListView.as_view(), name='certifico_list_pen'),
    path('certifico/list/',CertificoListView.as_view(), name='certifico_list'),
    path('certifico/<int:pk>/pdf/',PDF.as_view(), name='certifico_pdf'),
    path('certifico/create/', CertificoCreateView.as_view(), name='certifico_create'),
    path('certifico/<int:pk>/update/', CertificoUpdateView.as_view(), name='certifico_update'),
    path('certifico/<int:pk>/delete/', CertificoDeleteView.as_view(), name='certifico_delete'),
    path('certifico/<int:pk>/details/', CertificoDetailView.as_view(), name='certifico_detail'),
   
]

