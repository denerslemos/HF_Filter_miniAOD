import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

# initialize MessageLogger and output report

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                                # replace 'myfile.root' with the source file you want to use
                                fileNames = cms.untracked.vstring(
#		'file:/afs/cern.ch/work/d/ddesouza/Run2021/miniAOD/WORKWELL/CMSSW_11_2_0_pre6/src/withFilter.root'
		'file:/afs/cern.ch/work/d/ddesouza/Run2021/miniAOD/WORKWELL/CMSSW_11_2_X_2020-09-27-0000/src/reMiniAOD_DATA_PAT.root'
#	     'file:/afs/cern.ch/work/d/ddesouza/Run2021/miniAOD/NEWW/CMSSW_11_2_X_2020-07-12-2300/src/HeavyIonsAnalysis/Configuration/test/workstation/reMiniAOD_DATA_PAT.root'
#            'file:/afs/cern.ch/work/d/ddesouza/Run2021/miniAOD/work/prod/CMSSW_10_3_3_patch1/src/HeavyIonsAnalysis/Configuration/test/workstation/new/reMiniAOD_DATA_PAT.root'
#            'file:/afs/cern.ch/work/d/ddesouza/public/Cent_filter/reMiniAOD_DATA_PAT_withoutCentfilter.root'
                )
                            )

process.demo = cms.EDAnalyzer('DemoAnalyzer',
				filters           = cms.InputTag("hiHFfilters","hiHFfilters","PAT")
                              )

process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('test.root')
                                   )


process.p = cms.Path(process.demo)
