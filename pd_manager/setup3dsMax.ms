macroScript manager
category: "PdManager"
tooltip: "Pd Manager"
ButtonText: "SM"
icon: #("PdManager",1)
(
	python.Execute "from pd_manager import Sm3dsMax"
	python.Execute "Sm3dsMax.MainUI().show()"
)

macroScript saveVersion
category: "PdManager"
tooltip: "Pd Manager - Save Version"
ButtonText: "SM_SaveV"
icon: #("PdManager",2)
(
	python.Execute "from pd_manager import Sm3dsMax"
	python.Execute "Sm3dsMax.MainUI().saveAsVersionDialog()"
)

macroScript imageViewer
category: "PdManager"
tooltip: "Pd Manager - Image Viewer"
ButtonText: "ImageViewer"
icon: #("PdManager",4)
(
    python.Execute "from pd_manager import Sm3dsMax"
    python.Execute "pd_imageViewer = Sm3dsMax.MainUI()"
    python.Execute "pd_imageViewer.onIviewer()"
)

macroScript makePreview
category: "PdManager"
tooltip: "Pd Manager - Make Preview"
ButtonText: "Make Preview"
icon: #("PdManager",5)
(
	python.Execute "from pd_manager import Sm3dsMax"
	python.Execute "reload(Sm3dsMax)"
	python.Execute "Sm3dsMax.MaxManager().createPreview()"
)

macroScript projectMaterials
category: "PdManager"
tooltip: "Pd Manager - Project Materials"
ButtonText: "Project Materials"
icon: #("PdManager",6)
(
	python.Execute "from pd_manager import Sm3dsMax"
	python.Execute "pd_projectMaterials = Sm3dsMax.MainUI()"
	python.Execute "pd_projectMaterials.onPMaterials()"
)
