#slimming code
import PyCintex
import ROOT
from ROOT import (TFile,TDirectory,
                  TChain,TTree,TH1D)
#

TTree.SetMaxTreeSize( 5 * 1024 * 1024 * 1024 )

import sys
print "sys.argv = ", sys.argv

if not len(sys.argv)>=2:  raise(Exception, "Must specify inputFiles as argument!")
    
INPUTDATA = sys.argv[1].split(',')
print "inputFiles = ", INPUTDATA

h_mcevtweight = TH1D("h_mcevtweight","h_mcevtweight",75,-6000E3,6000E3)

#######################################################################
#
# Select branches from the TTree
#
#######################################################################
def selectBranches(TREE):
    TREE.SetBranchStatus("*",0); 
    TREE.SetBranchStatus("*PerXing",1);
    TREE.SetBranchStatus("vxp*",1);
    TREE.SetBranchStatus("RunNumber",1);
    TREE.SetBranchStatus("EventNumber",1);
    TREE.SetBranchStatus("lbn",1);
    TREE.SetBranchStatus("bcid",1);    
    TREE.SetBranchStatus("larError",1);
    TREE.SetBranchStatus("tileError", 1);
    TREE.SetBranchStatus("coreFlags", 1);  
    TREE.SetBranchStatus("tileFlags", 1);
    TREE.SetBranchStatus("Eventshape*",1);
    TREE.SetBranchStatus("top_hfor_type",1);
    TREE.SetBranchStatus("isSimulation",1);
    TREE.SetBranchStatus("timestamp",1);
    TREE.SetBranchStatus("timestamp_ns",1);
    TREE.SetBranchStatus("musp_n",1);
    TREE.SetBranchStatus("musp_eta",1);    
    TREE.SetBranchStatus("musp_phi",1);
    TREE.SetBranchStatus("musp_innerSegments",1);
    TREE.SetBranchStatus("musp_middleSegments",1);
    TREE.SetBranchStatus("musp_outerSegments",1);
    if TREE.GetBranch("mc_channel_number"):  TREE.SetBranchStatus("mc_channel_number", 1);
    if TREE.GetBranch("mc_event_number"):  TREE.SetBranchStatus("mc_event_number", 1);
    if TREE.GetBranch("mc_event_weight"):  TREE.SetBranchStatus("mc_event_weight", 1);
    if TREE.GetBranch("mcevt_n"):  TREE.SetBranchStatus("mcevt_n", 1);
    if TREE.GetBranch("mcevt_weight"): TREE.SetBranchStatus("mcevt_weight", 1);
    if TREE.GetBranch("mcevt_signal_process_id"):  TREE.SetBranchStatus("mcevt_signal_process_id", 1);
    if TREE.GetBranch("mcevt_event_number"): TREE.SetBranchStatus("mcevt_event_number", 1);
    if TREE.GetBranch("mcevt_event_scale"): TREE.SetBranchStatus("mcevt_event_scale", 1);
    if TREE.GetBranch("mcevt_alphaQCD"): TREE.SetBranchStatus("mcevt_alphaQCD", 1);
    if TREE.GetBranch("mcevt_alphaQED"): TREE.SetBranchStatus("mcevt_alphaQED", 1);
    if TREE.GetBranch("mcevt_pdf_id1"): TREE.SetBranchStatus("mcevt_pdf_id1", 1);
    if TREE.GetBranch("mcevt_pdf_id2"): TREE.SetBranchStatus("mcevt_pdf_id2", 1);
    if TREE.GetBranch("mcevt_pdf_x1"): TREE.SetBranchStatus("mcevt_pdf_x1", 1);
    if TREE.GetBranch("mcevt_pdf_x2"): TREE.SetBranchStatus("mcevt_pdf_x2", 1);
    if TREE.GetBranch("mcevt_pdf_scale"): TREE.SetBranchStatus("mcevt_pdf_scale", 1);        
    if TREE.GetBranch("mcevt_pdf1"): TREE.SetBranchStatus("mcevt_pdf1", 1);
    if TREE.GetBranch("mcevt_pdf2"): TREE.SetBranchStatus("mcevt_pdf2", 1);
    TREE.SetBranchStatus("mu_*",0);
    TREE.SetBranchStatus("mu_n",1);
    TREE.SetBranchStatus("mu_author",1);
    TREE.SetBranchStatus("mu_medium",1);
    TREE.SetBranchStatus("mu_tight",1);
    TREE.SetBranchStatus("mu_loose",1);
    TREE.SetBranchStatus("mu_eta",1);
    TREE.SetBranchStatus("mu_pt",1);
    TREE.SetBranchStatus("mu_px",1);
    TREE.SetBranchStatus("mu_py",1);
    TREE.SetBranchStatus("mu_pz",1);
    TREE.SetBranchStatus("mu_phi",1);
    TREE.SetBranchStatus("mu_E",1);
    TREE.SetBranchStatus("mu_m",1);
    TREE.SetBranchStatus("mu_isCombinedMuon",1);
    TREE.SetBranchStatus("mu_isSegmentTaggedMuon",1);
    TREE.SetBranchStatus("mu_isStandAloneMuon",1);
    TREE.SetBranchStatus("mu_ms_phi",1);
    TREE.SetBranchStatus("mu_ms_theta",1);
    TREE.SetBranchStatus("mu_trackz0pvunbiased",1);
    TREE.SetBranchStatus("mu_tracksigz0pvunbiased",1);
    TREE.SetBranchStatus("mu_momentumBalanceSignificance",1);
    TREE.SetBranchStatus("mu_allauthor",1);
    TREE.SetBranchStatus("mu_isCaloMuonId",1);
    TREE.SetBranchStatus("mu_isSiliconAssociatedForwardMuon",1);
    TREE.SetBranchStatus("mu_matchchi2",1);
    TREE.SetBranchStatus("mu_matchndof",1);
    TREE.SetBranchStatus("mu_scatteringCurvatureSignificance",1);
    TREE.SetBranchStatus("mu_scatteringNeighbourSignificance",1);
    TREE.SetBranchStatus("mu_momentumBalanceSignificance",1);
    TREE.SetBranchStatus("mu_energyLossPar",1);
    TREE.SetBranchStatus("mu_energyLossErr",1);
    TREE.SetBranchStatus("mu_etCore",1);
    TREE.SetBranchStatus("mu_energyLossType",1);
    TREE.SetBranchStatus("mu_caloLRLikelihood",1);
    TREE.SetBranchStatus("mu_nprecisionLayers",1);
    TREE.SetBranchStatus("mu_expectBLayerHit",1);
    TREE.SetBranchStatus("mu_nBLHits",1);
    TREE.SetBranchStatus("mu_nPixHits",1); 
    TREE.SetBranchStatus("mu_nPixelDeadSensors",1); 
    TREE.SetBranchStatus("mu_nSCTHits",1);
    TREE.SetBranchStatus("mu_nSCTDeadSensors",1); 
    TREE.SetBranchStatus("mu_nPixHoles",1); 
    TREE.SetBranchStatus("mu_nSCTHoles",1); 
    TREE.SetBranchStatus("mu_nTRTHits",1); 
    TREE.SetBranchStatus("mu_nTRTOutliers",1);
    TREE.SetBranchStatus("mu_nTRTHighTHits",1);
    TREE.SetBranchStatus("mu_nprecisionHoleLayers",1);
    TREE.SetBranchStatus("mu_nphiLayers",1);
    TREE.SetBranchStatus("mu_ntrigEtaLayers",1);
    TREE.SetBranchStatus("mu_nphiHoleLayers",1);
    TREE.SetBranchStatus("mu_ntrigEtaHoleLayers",1);
    TREE.SetBranchStatus("mu_charge",1);
    TREE.SetBranchStatus("mu_me_qoverp",1);
    TREE.SetBranchStatus("mu_id_qoverp",1);
    TREE.SetBranchStatus("mu_cb_d0_exPV",1);
    TREE.SetBranchStatus("mu_cb_z0_exPV",1);
    TREE.SetBranchStatus("mu_cb_phi_exPV",1);
    TREE.SetBranchStatus("mu_cb_theta_exPV",1);
    TREE.SetBranchStatus("mu_cb_qoverp_exPV",1);
    TREE.SetBranchStatus("mu_id_d0_exPV",1);
    TREE.SetBranchStatus("mu_id_z0_exPV",1);
    TREE.SetBranchStatus("mu_id_phi_exPV",1);
    TREE.SetBranchStatus("mu_id_theta_exPV",1);
    TREE.SetBranchStatus("mu_id_qoverp_exPV",1);
    TREE.SetBranchStatus("mu_me_d0_exPV",1);
    TREE.SetBranchStatus("mu_me_z0_exPV",1);
    TREE.SetBranchStatus("mu_me_phi_exPV",1);
    TREE.SetBranchStatus("mu_me_theta_exPV",1);
    TREE.SetBranchStatus("mu_me_qoverp_exPV",1);
    TREE.SetBranchStatus("mu_cb_d0",1);
    TREE.SetBranchStatus("mu_cb_z0",1);
    TREE.SetBranchStatus("mu_cb_phi",1);
    TREE.SetBranchStatus("mu_cb_theta",1);
    TREE.SetBranchStatus("mu_cb_qoverp",1);
    TREE.SetBranchStatus("mu_id_d0",1);
    TREE.SetBranchStatus("mu_id_z0",1);
    TREE.SetBranchStatus("mu_id_phi",1);
    TREE.SetBranchStatus("mu_id_theta",1);
    TREE.SetBranchStatus("mu_me_d0",1);
    TREE.SetBranchStatus("mu_me_z0",1);
    TREE.SetBranchStatus("mu_me_phi",1);
    TREE.SetBranchStatus("mu_me_theta",1);
    TREE.SetBranchStatus("mu_ptcone20",1);
    TREE.SetBranchStatus("mu_ptcone30",1);
    TREE.SetBranchStatus("mu_ptcone40",1);  
    TREE.SetBranchStatus("mu_etcone20",1);
    TREE.SetBranchStatus("mu_etcone30",1);
    TREE.SetBranchStatus("mu_etcone40",1);   
    TREE.SetBranchStatus("mu_trackd0pvunbiased",1);
    TREE.SetBranchStatus("mu_tracksigd0pvunbiased",1);
    TREE.SetBranchStatus("mu_tracktheta",1);
    TREE.SetBranchStatus("mu_trackd0",1);
    TREE.SetBranchStatus("mu_trackz0",1);
    TREE.SetBranchStatus("mu_trackphi",1);
    TREE.SetBranchStatus("mu_tracktheta",1);
    TREE.SetBranchStatus("mu_trackqoverp",1);
    TREE.SetBranchStatus("mu_trackcov_d0",1);
    TREE.SetBranchStatus("mu_trackcov_z0",1);
    TREE.SetBranchStatus("mu_trackcov_phi",1);
    TREE.SetBranchStatus("mu_trackcov_theta",1);
    TREE.SetBranchStatus("mu_trackcov_qoverp",1);
    TREE.SetBranchStatus("mu_trackcov_d0_z0",1);
    TREE.SetBranchStatus("mu_trackcov_d0_phi",1);
    TREE.SetBranchStatus("mu_trackcov_d0_theta",1);
    TREE.SetBranchStatus("mu_trackcov_d0_qoverp",1);
    TREE.SetBranchStatus("mu_trackcov_z0_phi",1);
    TREE.SetBranchStatus("mu_trackcov_z0_theta",1);
    TREE.SetBranchStatus("mu_trackcov_z0_qoverp",1);
    TREE.SetBranchStatus("mu_trackcov_phi_theta",1);
    TREE.SetBranchStatus("mu_trackcov_phi_qoverp",1);
    TREE.SetBranchStatus("mu_trackcov_theta_qoverp",1);
    TREE.SetBranchStatus("jet_AntiKt4TopoEM*",1);
    TREE.SetBranchStatus("jet_AntiKt4LCTopo*",1);
    TREE.SetBranchStatus("jet_AntiKt4TopoEM_flavor_*",0);
    TREE.SetBranchStatus("jet_AntiKt4LCTopo_flavor_*",0);
    TREE.SetBranchStatus("jet_AntiKt4TopoEM_flavor_weight*",1);
    TREE.SetBranchStatus("jet_AntiKt4LCTopo_flavor_weight*",1);
    TREE.SetBranchStatus("jet_AntiKt4LCTopo_flavor_component_jfitc_p*",1);
    TREE.SetBranchStatus("jet_AntiKt4LCTopo_flavor_component_jfitcomb_p*",1);
    TREE.SetBranchStatus("trig_Nav_n",1);
    TREE.SetBranchStatus("trig_Nav_chain_ChainId",1);
    TREE.SetBranchStatus("trig_Nav_chain_RoIType",1);
    TREE.SetBranchStatus("trig_Nav_chain_RoIIndex",1);
    if TREE.GetBranch("EF_2mu13"):  TREE.SetBranchStatus("EF_2mu13",1);
    if TREE.GetBranch("EF_mu24i_tight"): TREE.SetBranchStatus("EF_mu24i_tight",1);
    if TREE.GetBranch("EF_mu36_tight"): TREE.SetBranchStatus("EF_mu36_tight",1);
    if TREE.GetBranch("EF_mu18_tight_mu8_EFFS"): TREE.SetBranchStatus("EF_mu18_tight_mu8_EFFS",1);
    if TREE.GetBranch("EF_mu24_tight_mu6_EFFS"): TREE.SetBranchStatus("EF_mu24_tight_mu6_EFFS",1);
    if TREE.GetBranch("EF_mu18_tight_e7_medium1"): TREE.SetBranchStatus("EF_mu18_tight_e7_medium1",1);
    if TREE.GetBranch("trig_RoI_EF_mu_Muon_ROI"): TREE.SetBranchStatus("trig_RoI_EF_mu_Muon_ROI",1);
    if TREE.GetBranch("trig_RoI_EF_mu_TrigMuonEFInfoContainer"): TREE.SetBranchStatus("trig_RoI_EF_mu_TrigMuonEFInfoContainer",1);
    if TREE.GetBranch("trig_RoI_EF_mu_TrigMuonEFInfoContainerStatus"): TREE.SetBranchStatus("trig_RoI_EF_mu_TrigMuonEFInfoContainerStatus",1);
    if TREE.GetBranch("trig_RoI_L2_mu_CombinedMuonFeature"): TREE.SetBranchStatus("trig_RoI_L2_mu_CombinedMuonFeature",1);
    if TREE.GetBranch("trig_RoI_L2_mu_CombinedMuonFeatureStatus"): TREE.SetBranchStatus("trig_RoI_L2_mu_CombinedMuonFeatureStatus",1);
    if TREE.GetBranch("trig_RoI_L2_mu_MuonFeature"): TREE.SetBranchStatus("trig_RoI_L2_mu_MuonFeature",1);
    if TREE.GetBranch("trig_RoI_L2_mu_Muon_ROI"): TREE.SetBranchStatus("trig_RoI_L2_mu_Muon_ROI",1);
    if TREE.GetBranch("trig_EF_trigmuonef_track_CB_pt"): TREE.SetBranchStatus("trig_EF_trigmuonef_track_CB_pt",1);
    if TREE.GetBranch("trig_EF_trigmuonef_track_CB_eta"): TREE.SetBranchStatus("trig_EF_trigmuonef_track_CB_eta",1);
    if TREE.GetBranch("trig_EF_trigmuonef_track_CB_phi"): TREE.SetBranchStatus("trig_EF_trigmuonef_track_CB_phi",1);
    if TREE.GetBranch("trig_EF_trigmuonef_track_SA_pt"): TREE.SetBranchStatus("trig_EF_trigmuonef_track_SA_pt",1);
    if TREE.GetBranch("trig_EF_trigmuonef_track_SA_eta"): TREE.SetBranchStatus("trig_EF_trigmuonef_track_SA_eta",1);
    if TREE.GetBranch("trig_EF_trigmuonef_track_SA_phi"): TREE.SetBranchStatus("trig_EF_trigmuonef_track_SA_phi",1);
    if TREE.GetBranch("trig_EF_trigmugirl_track_CB_pt"): TREE.SetBranchStatus("trig_EF_trigmugirl_track_CB_pt",1);
    if TREE.GetBranch("trig_EF_trigmugirl_track_CB_eta"): TREE.SetBranchStatus("trig_EF_trigmugirl_track_CB_eta",1);
    if TREE.GetBranch("trig_EF_trigmugirl_track_CB_phi"): TREE.SetBranchStatus("trig_EF_trigmugirl_track_CB_phi",1);
    if TREE.GetBranch("trig_EF_trigmuonef_track_MuonType"): TREE.SetBranchStatus("trig_EF_trigmuonef_track_MuonType",1);
    if TREE.GetBranch("trig_L2_combmuonfeature_eta"): TREE.SetBranchStatus("trig_L2_combmuonfeature_eta",1);
    if TREE.GetBranch("trig_L2_combmuonfeature_phi"): TREE.SetBranchStatus("trig_L2_combmuonfeature_phi",1);
    if TREE.GetBranch("trig_L2_muonfeature_eta"): TREE.SetBranchStatus("trig_L2_muonfeature_eta",1);
    if TREE.GetBranch("trig_L2_muonfeature_phi"): TREE.SetBranchStatus("trig_L2_muonfeature_phi",1);
    if TREE.GetBranch("trig_L1_mu_eta"): TREE.SetBranchStatus("trig_L1_mu_eta",1);
    if TREE.GetBranch("trig_L1_mu_phi"): TREE.SetBranchStatus("trig_L1_mu_phi",1);
    if TREE.GetBranch("trig_L1_mu_thrName"): TREE.SetBranchStatus("trig_L1_mu_thrName",1);
    if TREE.GetBranch("trig_RoI_EF_mu_TrigMuonEFIsolationContainer"): TREE.SetBranchStatus("trig_RoI_EF_mu_TrigMuonEFIsolationContainer",1);
    if TREE.GetBranch("trig_RoI_EF_mu_TrigMuonEFIsolationContainerStatus"): TREE.SetBranchStatus("trig_RoI_EF_mu_TrigMuonEFIsolationContainerStatus",1);
    TREE.SetBranchStatus("tau_n", 1);
    TREE.SetBranchStatus("tau_Et", 1);
    TREE.SetBranchStatus("tau_pt", 1);
    TREE.SetBranchStatus("tau_m", 1);
    TREE.SetBranchStatus("tau_eta", 1);
    TREE.SetBranchStatus("tau_phi", 1);
    TREE.SetBranchStatus("tau_charge", 1);
    TREE.SetBranchStatus("tau_BDTEleScore", 1);
    TREE.SetBranchStatus("tau_BDTJetScore", 1);
    TREE.SetBranchStatus("tau_likelihood", 1);
    TREE.SetBranchStatus("tau_SafeLikelihood", 1);
    TREE.SetBranchStatus("tau_electronVetoLoose", 1);
    TREE.SetBranchStatus("tau_electronVetoMedium", 1);
    TREE.SetBranchStatus("tau_electronVetoTight", 1);
    TREE.SetBranchStatus("tau_muonVeto", 1);
    TREE.SetBranchStatus("tau_tauLlhLoose", 1);
    TREE.SetBranchStatus("tau_tauLlhMedium", 1);
    TREE.SetBranchStatus("tau_tauLlhTight", 1);
    TREE.SetBranchStatus("tau_JetBDTSigLoose", 1);
    TREE.SetBranchStatus("tau_JetBDTSigMedium", 1);
    TREE.SetBranchStatus("tau_JetBDTSigTight", 1);
    TREE.SetBranchStatus("tau_EleBDTLoose", 1);
    TREE.SetBranchStatus("tau_EleBDTMedium", 1);
    TREE.SetBranchStatus("tau_EleBDTTight", 1);
    TREE.SetBranchStatus("tau_author", 1);
    TREE.SetBranchStatus("tau_numTrack", 1);
    TREE.SetBranchStatus("tau_etOverPtLeadTrk", 1);
    TREE.SetBranchStatus("tau_leadTrkPt", 1);
    TREE.SetBranchStatus("tau_track_n", 1);
    TREE.SetBranchStatus("tau_track_eta", 1);
    TREE.SetBranchStatus("el_n", 1);
    TREE.SetBranchStatus("el_charge", 1);
    TREE.SetBranchStatus("el_author", 1);
    TREE.SetBranchStatus("el_isEM", 1);
    TREE.SetBranchStatus("el_OQ", 1);
    TREE.SetBranchStatus("el_loose", 1);
    TREE.SetBranchStatus("el_loosePP", 1);
    TREE.SetBranchStatus("el_medium", 1);
    TREE.SetBranchStatus("el_mediumPP", 1);
    TREE.SetBranchStatus("el_tight", 1);
    TREE.SetBranchStatus("el_tightPP", 1);
    TREE.SetBranchStatus("el_E237", 1);
    TREE.SetBranchStatus("el_E277", 1);
    TREE.SetBranchStatus("el_weta2", 1);
    TREE.SetBranchStatus("el_Etcone20", 1);
    TREE.SetBranchStatus("el_Etcone30", 1);
    TREE.SetBranchStatus("el_Etcone40", 1);
    TREE.SetBranchStatus("el_Etcone40_ED_corrected", 1);
    TREE.SetBranchStatus("el_ED_median", 1);
    TREE.SetBranchStatus("el_ptcone20", 1);
    TREE.SetBranchStatus("el_ptcone30", 1);
    TREE.SetBranchStatus("el_ptcone40", 1);
    TREE.SetBranchStatus("el_topoEtcone20", 1);
    TREE.SetBranchStatus("el_topoEtcone30", 1);
    TREE.SetBranchStatus("el_topoEtcone40", 1);
    TREE.SetBranchStatus("el_topoEtcone20_corrected", 1);
    TREE.SetBranchStatus("el_topoEtcone30_corrected", 1);
    TREE.SetBranchStatus("el_topoEtcone40_corrected", 1);
    TREE.SetBranchStatus("el_Etcone20_pt_corrected", 1);
    TREE.SetBranchStatus("el_Etcone30_pt_corrected", 1);
    TREE.SetBranchStatus("el_Etcone40_pt_corrected", 1);
    TREE.SetBranchStatus("el_expectHitInBLayer", 1);
    TREE.SetBranchStatus("el_pt", 1);
    TREE.SetBranchStatus("el_eta", 1);
    TREE.SetBranchStatus("el_phi", 1);
    TREE.SetBranchStatus("el_Es2", 1);
    TREE.SetBranchStatus("el_etap", 1);
    TREE.SetBranchStatus("el_etas2", 1);
    TREE.SetBranchStatus("el_phis2", 1);
    TREE.SetBranchStatus("el_cl_E", 1);
    TREE.SetBranchStatus("el_cl_pt", 1);
    TREE.SetBranchStatus("el_cl_eta", 1);
    TREE.SetBranchStatus("el_cl_phi", 1);
    TREE.SetBranchStatus("el_trackphi", 1);
    TREE.SetBranchStatus("el_trackpt", 1);
    TREE.SetBranchStatus("el_tracketa", 1);
    TREE.SetBranchStatus("el_nPixHits", 1);
    TREE.SetBranchStatus("el_nSCTHits", 1);
    TREE.SetBranchStatus("el_trackd0pv", 1);
    TREE.SetBranchStatus("el_trackz0pv", 1);
    TREE.SetBranchStatus("el_tracksigd0pv", 1);
    TREE.SetBranchStatus("el_tracksigz0pv", 1);
    TREE.SetBranchStatus("el_f3", 1);
    TREE.SetBranchStatus("el_Ethad", 1);
    TREE.SetBranchStatus("el_Ethad1", 1);
    TREE.SetBranchStatus("el_reta", 1);
    TREE.SetBranchStatus("el_f1", 1);
    TREE.SetBranchStatus("el_wstot", 1);
    TREE.SetBranchStatus("el_emaxs1", 1);
    TREE.SetBranchStatus("el_Emax2", 1);
    TREE.SetBranchStatus("el_deltaeta1", 1);
    TREE.SetBranchStatus("el_trackd0_physics", 1);
    TREE.SetBranchStatus("el_TRTHighTOutliersRatio", 1);
    TREE.SetBranchStatus("el_nTRTHits", 1);
    TREE.SetBranchStatus("el_nTRTOutliers", 1);
    TREE.SetBranchStatus("el_nSiHits", 1);
    TREE.SetBranchStatus("el_nSCTOutliers", 1);
    TREE.SetBranchStatus("el_nPixelOutliers", 1);
    TREE.SetBranchStatus("el_nBLHits", 1);
    TREE.SetBranchStatus("el_nBLayerOutliers", 1);
    TREE.SetBranchStatus("el_trackqoverp", 1);
    TREE.SetBranchStatus("el_deltaphi2", 1);
    TREE.SetBranchStatus("el_ED_median", 1);
    TREE.SetBranchStatus("el_trackd0pvunbiased", 1);
    TREE.SetBranchStatus("el_tracksigd0pvunbiased", 1);
    TREE.SetBranchStatus("el_rphi", 1);
    TREE.SetBranchStatus("el_refittedTrack_LMqoverp", 1);
    TREE.SetBranchStatus("el_refittedTrack_author", 1);
    TREE.SetBranchStatus("el_deltaphiRescaled", 1);
    TREE.SetBranchStatus("el_nPixelDeadSensors", 1);
    TREE.SetBranchStatus("el_nSCTDeadSensors", 1);
    TREE.SetBranchStatus("el_rawcl_Es0", 1);
    TREE.SetBranchStatus("el_rawcl_Es1", 1);
    TREE.SetBranchStatus("el_rawcl_Es2", 1);
    TREE.SetBranchStatus("el_rawcl_Es3", 1);
    TREE.SetBranchStatus("el_cl_etaCalo", 1);
    TREE.SetBranchStatus("el_cl_phiCalo", 1);
    TREE.SetBranchStatus("el_nTRTHighTHits", 1)
    TREE.SetBranchStatus("el_nTRTHighTOutliers", 1)
    TREE.SetBranchStatus("el_fside", 1)
    TREE.SetBranchStatus("el_ws3", 1)
    TREE.SetBranchStatus("el_trackz0pvunbiased", 1)
    TREE.SetBranchStatus("EF_g35_loose_g25_loose",1);
    TREE.SetBranchStatus("EF_2g20vh_medium",1);
    TREE.SetBranchStatus("el_type",1);
    TREE.SetBranchStatus("el_origin",1);
    TREE.SetBranchStatus("el_originbkg",1);
    TREE.SetBranchStatus("el_isEMLoose",1);
    TREE.SetBranchStatus("el_isEMMedium",1);
    TREE.SetBranchStatus("el_isEMTight",1);
    TREE.SetBranchStatus("*MET*",0);
    TREE.SetBranchStatus("MET_CellOut_Eflow_phi",1);
    TREE.SetBranchStatus("MET_RefFinal_et",1);
    TREE.SetBranchStatus("MET_RefFinal_etx",1);
    TREE.SetBranchStatus("MET_RefFinal_ety",1);
    TREE.SetBranchStatus("MET_RefFinal_sumet",1);
    TREE.SetBranchStatus("MET_RefFinal_STVF_et",1);
    TREE.SetBranchStatus("MET_RefFinal_STVF_etx",1);
    TREE.SetBranchStatus("MET_RefFinal_STVF_ety",1);
    TREE.SetBranchStatus("MET_RefFinal_STVF_sumet",1);
    TREE.SetBranchStatus("MET_RefTau_etx",1);
    TREE.SetBranchStatus("MET_RefTau_ety",1);
    TREE.SetBranchStatus("MET_RefTau_sumet",1);
    TREE.SetBranchStatus("MET_RefJet_etx",1);
    TREE.SetBranchStatus("MET_RefJet_ety",1);
    TREE.SetBranchStatus("MET_RefJet_sumet",1);
    TREE.SetBranchStatus("MET_RefGamma_etx",1);
    TREE.SetBranchStatus("MET_RefGamma_ety",1);
    TREE.SetBranchStatus("MET_RefGamma_sumet",1);
    TREE.SetBranchStatus("MET_RefMuon_etx",1);
    TREE.SetBranchStatus("MET_RefMuon_ety",1);
    TREE.SetBranchStatus("MET_RefMuon_sumet",1);
    TREE.SetBranchStatus("MET_RefMuon_Muid_etx",1);
    TREE.SetBranchStatus("MET_RefMuon_Muid_ety",1);
    TREE.SetBranchStatus("MET_RefMuon_Muid_sumet",1);
    TREE.SetBranchStatus("MET_CellOut_Eflow_STVF_etx",1);
    TREE.SetBranchStatus("MET_CellOut_Eflow_STVF_ety",1);
    TREE.SetBranchStatus("MET_CellOut_Eflow_STVF_sumet",1);
    TREE.SetBranchStatus("MET_CellOut_Eflow_STVF_et",1);
    TREE.SetBranchStatus("MET_CellOut_Eflow_etx",1);
    TREE.SetBranchStatus("MET_CellOut_Eflow_ety",1);
    TREE.SetBranchStatus("MET_CellOut_Eflow_sumet",1);
    TREE.SetBranchStatus("MET_CellOut_Eflow_et",1);
    TREE.SetBranchStatus("jet_AntiKt4LCTopo_MET_wpx",1);
    TREE.SetBranchStatus("jet_AntiKt4LCTopo_MET_wpy",1);
    TREE.SetBranchStatus("jet_AntiKt4LCTopo_MET_wet",1);
    TREE.SetBranchStatus("jet_AntiKt4LCTopo_MET_statusWord",1);
    TREE.SetBranchStatus("jet_AntiKt4LCTopo_MET_n",1);
    TREE.SetBranchStatus("mu_MET_n",1);
    TREE.SetBranchStatus("mu_MET_wet",1);
    TREE.SetBranchStatus("mu_MET_wpx",1);
    TREE.SetBranchStatus("mu_MET_wpy",1);
    TREE.SetBranchStatus("mu_MET_statusWord",1);
    TREE.SetBranchStatus("mu_staco_MET_wet",1);
    TREE.SetBranchStatus("mu_staco_MET_wpx",1);
    TREE.SetBranchStatus("mu_staco_MET_wpy",1);
    TREE.SetBranchStatus("mu_staco_MET_statusWord",1);
    TREE.SetBranchStatus("el_MET_wet",1);
    TREE.SetBranchStatus("el_MET_wpx",1);
    TREE.SetBranchStatus("el_MET_wpy",1);
    TREE.SetBranchStatus("el_MET_statusWord",1);
    TREE.SetBranchStatus("tau_MET_wet",1);
    TREE.SetBranchStatus("tau_MET_wpx",1);
    TREE.SetBranchStatus("tau_MET_wpy",1);
    TREE.SetBranchStatus("tau_MET_statusWord",1);
    if TREE.GetBranch("mc_pt"): TREE.SetBranchStatus("mc_*", 1);
    if TREE.GetBranch("mc_t_vx_n"): TREE.SetBranchStatus("mc_t*", 0);
    if TREE.GetBranch("mc_Z_vx_n"): TREE.SetBranchStatus("mc_Z*", 0);
    if TREE.GetBranch("mc_W_vx_n"): TREE.SetBranchStatus("mc_W*", 0);
    if TREE.GetBranch("AntiKt4TruthWithMuNu_pt"): TREE.SetBranchStatus("AntiKt4TruthWithMuNu_*", 1);
  
    return

#######################################################################
#
# Create Chains
#
#######################################################################
evtTreeName = "physics"
metaName = evtTreeName+"Meta"

evtChain =TChain(evtTreeName)
metaChain=TChain(metaName+"/TrigConfTree")
[map(i.Add,INPUTDATA) for i in [evtChain,metaChain]]

# empty input
print " number of events ",  evtChain.GetEntries()

if evtChain.GetEntries()==0:
    g=TFile("skim.root","RECREATE")
    newTree=ROOT.TTree("physics","physics")
    newTree.Write()
    exit()

# Select Events with cuts
nEntries = evtChain.GetEntries()
EntryList_2l=ROOT.TEntryList()
for i in range(nEntries):
    evtChain.GetEntry(i)
    nmu=evtChain.mu_n
    nmc=evtChain.mc_n
    ngoodmu=0
    ntruthlep=0
    h_mcevtweight.Fill(1,1);
    for j in range(nmc):
        if not (evtChain.mc_barcode[j]<200000 and evtChain.mc_status[j]==1): continue
        if ((abs(evtChain.mc_pdgId[j])==13 and evtChain.mc_pt[j]>=15000 and abs(evtChain.mc_eta[j]) <2.6)):
           ntruthlep=ntruthlep+1
    for j in range(nmu):
        if not ((not evtChain.mu_isStandAloneMuon[j]) and evtChain.mu_pt[j] > 15000 and abs(evtChain.mu_eta[j]) <2.6): continue
        ngoodmu=ngoodmu+1
  
    if (ngoodmu>=2 or ntruthlep>=2):
        EntryList_2l.Enter(i,evtChain)
 
evtChain.SetEntryList(EntryList_2l)

#######################################################################
#
# Select and write out
#
#######################################################################
selectBranches(evtChain)
g=TFile("skim.root","RECREATE")

nEntries = evtChain.GetEntries()

newTree=evtChain.CopyTree("","fast SortBasketsByEntry")

""" 
newTree=evtChain.CopyTree("%s && %s" % (GRL,CUTEVENT),"fast SortBasketsByEntry")
# only do the following if root v5.26
try: newTree.OptimizeBaskets(10000000, 1.1, "d")
except:
    print " OptimizeBaskets not working " 
    pass

#newTree.BuildIndex("trig_DB_SMK","lbn")

""" 
newTree.Write()
h_mcevtweight.Write()
#
g.mkdir(metaName); g.cd(metaName)
newMeta=metaChain.CloneTree(-1,"fast SortBasketsByEntry")
# only do the following if root v5.26
#try: newqcdMeta.OptimizeBaskets(10000000, 1.1, "d")
#except:
#    print " OptimizeBaskets not working " 
#    pass
#newMeta.BuildIndex("SMK","L1PSK")
#newMeta.Write()
#g.Close()

