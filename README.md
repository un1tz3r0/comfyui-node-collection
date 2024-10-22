# ComfyUI Node Collection
#### 900+ custom-nodes add-ons for ComfyUI

<!--
This repository contains a very large collection of comfyui custom nodes, ~13GB, over 900 items in the repository root.

Don't even try to load all of these at once... I did, spent 3+ hours fixing missing dependencies and ripping custom nodes out when that didn't clear an error, and after a while I got it to stop crashing out, but even after a solid hour it was still not even done starting up, so I'd say these are probably more useful when selectively enabled.

**Disclaimer**: Use these at your own risk. There may well be some malicious code hiding somewhere in there, 13GB is alot of python code and I do not have time to personally comb through it all. Precautions and safety measures (sandboxing, venvs, security contexts, chroots, virtual machines) are strongly reccomended when using these or any other executable code from the internets.

Here is a listing... enjoy.
-->

This repo is a gold mine for ComfyUI users. It contains a ton of custom nodes, and I mean a ton (~13GB, before the first-run setup downloads and dependency installs). I think there’s over 900 items here! So many it would take forever to load them all at once, and I don’t think I’d ever want to. It’s better to just pick and choose the ones you need for a particular project. 

A word of warning, though: I have no idea what’s actually in these files, and there are so many of them that I can’t imagine anyone has gone through all of them. You never know what you’re going to get when you’re downloading code from the internet, so be careful.

Here's what's in the custom-nodes subdirectory currently:

 - 0_FutureWarningIgnore.py
 - A8R8_ComfyUI_nodes
 - abg-comfyui
 - abracadabra-comfyui
 - advance-aesthetic-score
 - aegisflow_utility_nodes
 - AIGODLIKE-ComfyUI-Studio
 - AIGODLIKE-COMFYUI-TRANSLATION
 - AIvector.py
 - alkemann.py
 - ambw_comfyui
 - antrobots-comfyUI-nodepack
 - anynode
 - a-person-mask-generator
 - As_ComfyUI_CustomNodes
 - ASTERR
 - asymmetric-tiling-comfyui
 - attention-couple-ComfyUI
 - avatar-graph-comfyui
 - Batch-Condition-ComfyUI
 - batchImg-rembg-ComfyUI-nodes
 - bilbox-comfyui
 - braintacles-comfyui-nodes
 - BrevLoadImage.py
 - bsz-cui-extras
 - canvas_tab
 - cd-tuner_negpip-ComfyUI
 - cgem156-ComfyUI
 - cg-image-picker
 - cg-noise
 - cg-prompt-info
 - cg-use-everywhere
 - Chaosaiart-Nodes
 - CharacterFaceSwap
 - chatbox_overlay.py
 - clipseg.py
 - clip_text_encoder_a1111.py
 - clip_text_encode_split.py
 - color2rgb.py
 - comfy_clip_blip_node
 - comfy-easy-grids
 - comfygen
 - comfy_http_request
 - ComfyI2I
 - comfy-image-saver
 - Comfy_KepKitchenSink
 - Comfy_KepListStuff
 - Comfy_KepMatteAnything
 - comfykit-custom-nodes
 - Comfy-LFO
 - ComfyLiterals
 - ComfyMath
 - comfy-mecha
 - comfy_mtb
 - comfy-nodes
 - comfy-pants
 - Comfy-Photoshop-SD
 - comfy_pixelization
 - comfy-plasma
 - comfy_PoP
 - ComfyQR
 - ComfyQR-scanning-nodes
 - Comfy-RVC
 - ComfyS3
 - Comfy-Topaz
 - ComfyUI
 - ComfyUI-0246
 - ComfyUI-3D-Pack
 - ComfyUI_3dPoseEditor
 - comfyui_ab_samplercustom
 - ComfyUI_AceNodes
 - ComfyUI-ADMotionDirector
 - ComfyUI-Advanced-ControlNet
 - ComfyUI-Advanced-Latent-Control
 - ComfyUI_ADV_CLIP_emb
 - comfyui-aesthetic-predictor-v2-5
 - ComfyUI-aichemy-nodes
 - ComfyUI-Aimidi-nodes
 - ComfyUI-AIT
 - ComfyUI_alkaid
 - ComfyUI-Allor
 - ComfyUI-Anchors
 - ComfyUI-AnimateAnyone-Evolved
 - ComfyUI-AnimateAnyone-reproduction
 - comfyui-animatediff
 - ComfyUI-AnimateDiff-Evolved
 - comfyui-anime-seg
 - ComfyUI_Aniportrait
 - ComfyUI-AniPortrait
 - ComfyUI-Anyline
 - ComfyUI_API_Manager
 - ComfyUI-APISR
 - ComfyUI-APISR-KJ
 - ComfyUI-ArtGallery
 - comfyui-art-venture
 - ComfyUI_aspect_ratios
 - ComfyUI-Assistant
 - ComfyUI-AudioReactive
 - ComfyUI-AudioReactor
 - ComfyUI-AudioScheduler
 - ComfyUI-AutoColorGimp
 - ComfyUI-AutoCropFaces
 - comfyui_auto_danbooru
 - ComfyUI-AutoLabel
 - ComfyUI-AutomaticCFG
 - comfyui-auto-nodes-layout
 - ComfyUI-AutoTrimBG
 - ComfyUI-Background-Replacement
 - ComfyUI_BadgerTools
 - comfyui-base64-to-image
 - ComfyUI_BattlemapGrid
 - ComfyUI-Better-Strings
 - ComfyUI-BiRefNet
 - ComfyUI-BiRefNet-ZHO
 - ComfyUI-bleh
 - ComfyUI_Blender_Texdiff
 - comfyui_bmab
 - ComfyUI-Bmad-DirtyUndoRedo
 - comfyui_bmad_nodes
 - ComfyUI-Book-Tools
 - ComfyUI-BRIA_AI-RMBG
 - ComfyUI-Bringing-Old-Photos-Back-to-Life
 - comfyui-browser
 - ComfyUI-BrushNet
 - ComfyUI-BrushNet-Wrapper
 - comfyui-caching-embeddings
 - ComfyUI-CADS
 - ComfyUI-Calculation
 - ComfyUI-CameraCtrl-Wrapper
 - ComfyUI_CartoonSegmentation
 - ComfyUI-CascadeResolutions
 - ComfyUI-Catcat
 - ComfyUI-CCSR
 - ComfyUI-CenterNode
 - ComfyUI-Champ
 - ComfyUI_Change_IMAGE_BOREDER
 - ComfyUI_ChatGLM_API
 - ComfyUI-Chat-GPT-Integration
 - comfyui-checkpoint-automatic-config
 - ComfyUI-Chibi-Nodes
 - ComfyUI-ClarityAI
 - comfyui-clear-screen
 - ComfyUI-ClipScore-Nodes
 - comfyui-clip-with-break
 - ComfyUI-Cloud
 - comfyui_cohere
 - ComfyUI_ColorImageDetection
 - ComfyUI_ColorMod
 - ComfyUI-ComfyCouple
 - ComfyUI_Comfyroll_CustomNodes
 - ComfyUI-ComfyRun
 - ComfyUI-ComfyWorkflows
 - ComfyUI-Comic
 - comfyui-consistency-decoder
 - comfyui_controlnet_aux
 - ComfyUI-ControlnetAux
 - ComfyUI-CoreMLSuite
 - ComfyUI-Coziness
 - ComfyUI-Cre8it-Nodes
 - ComfyUI-Crystools
 - ComfyUI-Crystools-save
 - ComfyUI_cspnodes
 - ComfyUI-CSV-Loader
 - ComfyUI-CUP
 - ComfyUI_CustomNet
 - comfyui-custom-nodes
 - ComfyUI-Custom-Nodes
 - ComfyUI_Custom_Nodes_AlekPet
 - ComfyUI-CustomScheduler
 - ComfyUI-Custom-Scripts
 - ComfyUI_Cutoff
 - comfyui-cyclist
 - ComfyUI-d2-size-selector
 - ComfyUI-d2-steps
 - comfyui_dagthomas
 - ComfyUI_DanTagGen
 - ComfyUI-DARE-LoRA-Merge
 - ComfyUI-DareMerge
 - ComfyUI-Dart
 - ComfyUI-DDColor
 - ComfyUI_DDColor
 - ComfyUI-Debug
 - ComfyUI-deepcache
 - ComfyUI-Deepface
 - comfyUI-DeepSeek-2lab
 - comfyui-deploy
 - ComfyUI-Depth-Anything-Tensorrt
 - ComfyUI-depth-fm
 - ComfyUI-DepthFM
 - ComfyUI-Depth-Visualization
 - ComfyUI-Dev-Utils
 - ComfyUI-Diffusers
 - comfyui-diffusion-cg
 - ComfyUI-DiffusionLight
 - ComfyUI-dimension-node-modusCell
 - ComfyUI-DirGir
 - ComfyUI-Disco-Diffusion
 - comfyui-discopixel
 - ComfyUI_DiT
 - ComfyUI-dpmpp_2m_alt-Sampler
 - ComfyUI-DragAnything
 - ComfyUI-DragNUWA
 - ComfyUI_Dragos_Nodes
 - ComfyUI-Dream-Interpreter
 - comfyui-dream-project
 - ComfyUI_Dreamtalk
 - comfyui-dream-video-batches
 - ComfyUI-DRMN
 - comfyui_DSP_imagehelpers
 - ComfyUI-dust3r
 - comfyui-dynamicprompts
 - ComfyUI-DynamiCrafter
 - ComfyUI-DynamiCrafterWrapper
 - ComfyUI-Eagle-PNGInfo
 - ComfyUI_Eagleshadow
 - ComfyUI-EasyAnimate
 - comfyui-easyapi-nodes
 - ComfyUI-EasyDeforum
 - ComfyUI-EasyNode
 - comfyui_easy_padding
 - ComfyUI-Easy-Use
 - ComfyUI-ELLA
 - ComfyUI-ELLA-wrapper
 - ComfyUI-Embedding_Picker
 - ComfyUI-Embeddings-Tools
 - comfyui-enhanced-save-node
 - Comfyui-ergouzi-Nodes
 - ComfyUI_essentials
 - ComfyUI-ExLlama
 - ComfyUI-ExLlama-Nodes
 - ComfyUI_experiments
 - ComfyUI_ExtendedImageFormats
 - ComfyUI_ExtraModels
 - ComfyUI-Extra-Samplers
 - ComfyUI_ezXY
 - ComfyUI_fabric
 - ComfyUI_FaceAnalysis
 - ComfyUI-FaceChain
 - Comfyui-FaceCompare
 - comfyui-faceless-node
 - comfyui_face_parsing
 - ComfyUI_FaceSimilarity
 - ComfyUI-FaceSwap
 - comfyui_facetools
 - ComfyUI-fal-Connector
 - ComfyUI-Fans
 - ComfyUI-fastblend
 - ComfyUI_FastVAEDecorder_SDXL
 - ComfyUI-FatLabels
 - ComfyUI-FBCNN
 - comfyui-fb-utils
 - ComfyUI_Fictiverse
 - ComfyUI_Fill-Nodes
 - ComfyUI-FishSpeech
 - comfyui-fitsize
 - ComfyUI_FizzNodes
 - ComfyUI-FLATTEN
 - comfyui-floodgate
 - ComfyUI-Flowty-CRM
 - ComfyUI-Flowty-LDSR
 - ComfyUI-Flowty-TripoSR
 - ComfyUI_Fooocus_KSampler
 - ComfyUI-Frame-Interpolation
 - ComfyUI_FrameMaker
 - ComfyUI_fsdymy
 - ComfyUI-Gaffer
 - ComfyUI-GCP-Storage
 - Comfyui-Gelbooru
 - ComfyUI-Gemini
 - ComfyUI-Gemma
 - comfyui-geometry
 - ComfyUI-Geowizard
 - ComfyUI_GetFileNameFromURL
 - ComfyUI-GlifNodes
 - ComfyUI_GLM4Node
 - ComfyUI_GMIC
 - ComfyUI-GPEN
 - ComfyUI-GPT2P
 - ComfyUI-GPT4V-Image-Captioner
 - ComfyUI-GPT_SoVITS
 - ComfyUI-GPU-temperature-protection
 - ComfyUI_GradientDeepShrink
 - ComfyUI_GraftingRayman
 - ComfyUI-graphToPrompt
 - ComfyUI-Griptape
 - ComfyUI-Gtsuya-Nodes
 - ComfyUI-Hangover-Moondream
 - ComfyUI-Hangover-Nodes
 - ComfyUI-Hangover-Recognize_Anything
 - ComfyUI-Helper-Nodes
 - ComfyUI-HF
 - ComfyUI_HFDownLoad
 - ComfyUI-HfLoader
 - ComfyUI-HiDiffusion
 - ComfyUI_HiDiffusion_Pro
 - ComfyUI-Hiero-Nodes
 - comfyui-hiforce-plugin
 - ComfyUI-HQ-Image-Save
 - ComfyUI_hus_utils
 - ComfyUI-HyperSDXL1StepUnetScheduler
 - ComfyUI-I2VGEN-XL
 - ComfyUI_Ib_CustomNodes
 - ComfyUI-IC-Light
 - ComfyUI-IC-Light-Native
 - ComfyUI_ID_Animator
 - ComfyUI-IDM-VTON
 - ComfyUI-IF_AI_HFDownloaderNode
 - ComfyUI-IF_AI_tools
 - ComfyUI-IF_AI_WishperSpeechNode
 - ComfyUI-IG-Nodes
 - Comfyui_image2prompt
 - ComfyUI-Image-Browsing
 - ComfyUI-ImageCropper
 - ComfyUI-Image-Filters
 - ComfyUI-Image-Matting
 - ComfyUI_ImageProcessing
 - comfyui-Image-reward
 - ComfyUI-ImageReward
 - comfyui-image-round
 - ComfyUI-Image-Saver
 - ComfyUI-Image-Selector
 - ComfyUI-Image-Tools
 - ComfyUI_ImageToText
 - ComfyUI-ImageUploader
 - ComfyUI-Img2Img-Turbo
 - ComfyUI-IMG_Query
 - ComfyUI-Impact-Pack
 - ComfyUI_Inpaint
 - ComfyUI-Inpaint-CropAndStitch
 - comfyui-inpaint-nodes
 - ComfyUI-Inspire-Pack
 - ComfyUI-InstanceDiffusion
 - ComfyUI-InstantID
 - ComfyUI_InstantID
 - comfyui-instantId-faceswap
 - ComfyUI-InstantIDUtils
 - ComfyUI-InstantMesh
 - ComfyUI-InstructIR
 - ComfyUI_InterpolateEverything
 - ComfyUI-InversedNoise
 - ComfyUI_Invisible_Watermark
 - comfyui_io_helpers
 - ComfyUI_IPAdapter_plus
 - ComfyUI-IPAnimate
 - ComfyUI-IP_LAP
 - ComfyUI_IsaacNodes
 - ComfyUI-IsNiceParts
 - ComfyUI-Iterative-Mixer
 - ComfyUI-J
 - ComfyUI_Jags_Audiotools
 - ComfyUI_Jags_VectorMagic
 - comfyui_jankhidiffusion
 - ComfyUI-JaRue
 - ComfyUI-JDCN
 - ComfyUI-Jjk-Nodes
 - ComfyUI-JNodes
 - comfyui-job-iterator
 - Comfyui_joytag
 - ComfyUI_JPS-Nodes
 - comfyui-kandinsky22
 - ComfyUI-KepOpenAI
 - ComfyUI-kewky_tools
 - ComfyUI-Keyframe
 - ComfyUI-Keyframed
 - ComfyUI-KJNodes
 - ComfyUI_kkTranslator_nodes
 - comfyui_kmeans_filter
 - ComfyUI_KytraWebhookHTTP
 - Comfyui_Lama
 - comfyui-lama-remover
 - ComfyUI-Latent-Modifiers
 - ComfyUI_LatentToRGB
 - ComfyUI-LaVi-Bridge-Wrapper
 - ComfyUI-LaVIT
 - ComfyUI-layerdiffuse
 - ComfyUI-LayerDivider
 - ComfyUI-Layers
 - ComfyUI_LayerStyle
 - ComfyUI-LCM
 - ComfyUI-LexMSDBNodes
 - ComfyUI-LexTools
 - comfyui-liam
 - comfyui_liam_util
 - ComfyUI-LightGlue
 - ComfyUI_LightGradient
 - comfyui_lists_cartesian_product
 - ComfyUI_LiteLLM
 - ComfyUI-Live2DViewer
 - ComfyUI-Llama
 - ComfyUI_Llama3_8B
 - ComfyUI-LLaVA-Captioner
 - comfyui-llm-assistant
 - ComfyUI_LLM_Node
 - comfyui-llm-node-for-amazon-bedrock
 - comfyui_LLM_party
 - ComfyUI-LLMs
 - ComfyUI_LLMVISION
 - ComfyUI-load-image-from-url
 - comfyui-load-image-in-seq
 - comfyui-local-db
 - ComfyUI-Logic
 - ComfyUI-LogicUtils
 - ComfyUI-Login
 - ComfyUI-Long-CLIP
 - ComfyUI-Loopchain
 - ComfyUI-Lora-Auto-Trigger-Words
 - comfyui_lora_tag_loader
 - ComfyUI-LoRA-Tuner
 - ComfyUI-MagicAnimate
 - comfyui-magic-clothing
 - ComfyUI_MagicClothing
 - ComfyUI-MagickWand
 - ComfyUI-MakeFrame
 - ComfyUI-Malefish-Custom-Scripts
 - ComfyUI-Manager
 - ComfyUI-Mana-Nodes
 - ComfyUI-mape-Helpers
 - ComfyUI_MaraScott_Nodes
 - ComfyUI-Marigold
 - ComfyUI-MaskBatchPermutations
 - comfyui-mask-boundingbox
 - comfyui-mask-util
 - comfyui_meanshift_filter
 - ComfyUI_Memeplex_DALLE
 - comfyui-menu-anchor
 - ComfyUI-MeshMesh
 - ComfyUI_Mexx_Poster
 - ComfyUI_Mexx_Styler
 - ComfyUI_MileHighStyler
 - ComfyUI_MiniCPM-V
 - ComfyUI-Minio
 - ComfyUI_Mira
 - comfyui-mirror
 - comfyui-mixlab-nodes
 - ComfyUI-mnemic-nodes
 - ComfyUI-Mobile
 - ComfyUI-ModelDownloader
 - ComfyUI-Model-Manager
 - ComfyUI_ModelScopeT2V
 - ComfyUI_Mokkaboss1
 - ComfyUI-moondream
 - ComfyUI-Moore-AnimateAnyone
 - ComfyUI-Mosaica
 - ComfyUI-MotionCtrl
 - ComfyUI-MotionCtrl-SVD
 - ComfyUI-MotionDiff
 - ComfyUI-Motion-Vector-Extractor
 - ComfyUI_mozman_nodes
 - ComfyUI_MSSpeech_TTS
 - ComfyUI-MuseTalk
 - ComfyUI-MuseTalk_FSH
 - ComfyUI-MuseTalkUtils
 - ComfyUI-MuseV
 - comfyui_musev_evolved
 - ComfyUI_MX_post_processing-nodes
 - ComfyUI_NAIDGenerator
 - ComfyUI_Native_DynamiCrafter
 - comfyui-NDI
 - ComfyUI-NegiTools
 - ComfyUI_NetDist
 - ComfyUI-nevysha-top-menu
 - ComfyUI-ngrok
 - ComfyUI-Nich-Utils
 - ComfyUI_Nimbus-Pack
 - ComfyUi_NNLatentUpscale
 - ComfyUI-N-Nodes
 - ComfyUI_node_Lilly
 - ComfyUI-NodePresets
 - ComfyUI-NodeReset
 - comfyui-nodes-docs
 - ComfyUI-nodes-hnmr
 - ComfyUI-noEmbryo
 - ComfyUI_Noise
 - ComfyUi-NoodleWebcam
 - ComfyUI-Notifications
 - ComfyUI_NoxinNodes
 - comfyUI-nsfw-detection
 - ComfyUI-NSFW-Detection
 - ComfyUI-N-Sidebar
 - ComfyUI-off-suite
 - comfyui-ollama
 - ComfyUI-Ollama-Describer
 - ComfyUi-Ollama-YN
 - comfyui-oms-diffusion
 - ComfyUI-OOTDiffusion
 - ComfyUI_OOTDiffusion_CXH
 - ComfyUI-OpenAINode
 - ComfyUI-openpose-editor
 - ComfyUI-OpenPose-Editor
 - ComfyUI-Openpose-Editor-Plus
 - ComfyUI-OpenPose-Keypoint-Extractor
 - ComfyUI-Open-Sora
 - ComfyUI-Open-Sora-Plan
 - ComfyUI_OpenVoice
 - comfyui-optical-flow
 - ComfyUI-OtherVAEs
 - comfyui_otonx_nodes
 - ComfyUI-ownimage
 - comfyui-p2ldgan
 - comfyui-paint
 - ComfyUI-paint-by-example
 - ComfyUI-Panda3d
 - ComfyUI_ParlerTTS
 - ComfyUI-Path-Helper
 - ComfyUI-path-util
 - ComfyUI_PCDMs
 - ComfyUI_PerpWeight
 - ComfyUI-Pets
 - ComfyUI-Phi-3-mini
 - ComfyUI-PhotoMaker-Plus
 - ComfyUI-PhotoMaker-ZHO
 - comfyui-photoshop
 - ComfyUI_Pic2Story
 - ComfyUI-PickScore-Nodes
 - ComfyUI_Pilgram
 - ComfyUI_Pipeline_Tool
 - ComfyUI-PiperTTS
 - ComfyUI-PixArt-alpha-Diffusers
 - comfyui-pixel
 - ComfyUI-PixelArt-Detector
 - ComfyUI-PixelOE
 - ComfyUI-PNG-Metadata
 - comfyui-popup_preview
 - ComfyUI-Portrait-Maker
 - comfyui-portrait-master
 - comfyui-portrait-master-zh-cn
 - ComfyUI-PoseKeypoint-Mask
 - ComfyUI-post-processing-nodes
 - ComfyUI-Prediction
 - ComfyUI-Prediction-Boost
 - ComfyUI_Preset_Merger
 - comfyui-previewlatent
 - ComfyUI_Primere_Nodes
 - comfyui_private_postprocessor
 - comfyui-profiler
 - comfyui-PromptAttention
 - ComfyUI-Prompt-Combinator
 - comfyui-prompt-composer
 - comfyui-prompt-control
 - ComfyUI-Prompt-Expansion
 - comfyui-prompt-extranetworks
 - comfyui-prompt-format
 - ComfyUI-promptLAB
 - ComfyUI-Prompt-MZ
 - ComfyUI-PromptOrganizer
 - ComfyUI-Prompt-Preview
 - comfyui-prompt-reader-node
 - ComfyUi_PromptStylers
 - ComfyUI-PromptUtilities
 - ComfyUI-Pronodes
 - ComfyUI_ProPainter_Nodes
 - comfyui-propost
 - comfyui-psd2png
 - ComfyUI-Pymunk
 - ComfyUI_pytorch_openpose
 - comfyui-pzc-multiworkspace
 - ComfyUI-QaisHelper
 - ComfyUI-Q-Align
 - ComfyUI-quadMoons-nodes
 - ComfyUI-QualityOfLifeSuit_Omar92
 - comfyui_quilting
 - ComfyUI-Qwen-VL-API
 - comfyui_r44_nodes
 - ComfyUI-RAFT
 - comfyui-ramdom-node
 - comfyui-ranbooru
 - ComfyUI-RandomSize
 - ComfyUI-RAVE
 - ComfyUI-RAVE_ATTN
 - ComfyUI-RawSaver
 - comfyui-reactor-node
 - ComfyUI-RefSampling
 - comfyui-remote-tools
 - ComfyUI-Remover
 - ComfyUI-RenderRiftNodes
 - ComfyUI-RequestsPoster
 - ComfyUI_RErouter_CustomNodes
 - ComfyUI-ResAdapter
 - ComfyUI_ResolutionSelector
 - ComfyUI_restart_sampling
 - comfyui-rf-nodes
 - ComfyUI-ricing
 - comfyui-ricklove
 - ComfyUI_roop
 - ComfyUI_rotate_image
 - ComfyUI_RSS_Feed_Reader
 - ComfyUI-RuiquNodes
 - ComfyUI-RunRunRun
 - ComfyUI-RVC
 - ComfyUI-S3-Tools
 - ComfyUI-safety-checker
 - ComfyUI-SAI_API
 - Comfyui-SAL-VTON
 - ComfyUI-sampler-lcm-alternative
 - ComfyUI-SaveAsScript
 - ComfyUI-Saveaswebp
 - ComfyUI-SaveAVIF
 - comfyui-saveimage-plus
 - ComfyUI-SaveImageWithMetaData
 - ComfyUI-SaveImgPrompt
 - ComfyUI-SaveQueues
 - ComfyUI-ScenarioPrompt
 - ComfyUI-SceneGenerator
 - ComfyUI-SchedulerMixer
 - ComfyUI_SDXL_DreamBooth_LoRA_CustomNodes
 - ComfyUI-SDXL-EmptyLatentImage
 - ComfyUI-seam-carving
 - ComfyUI_Seamless_Patten
 - ComfyUI-seamless-tiling
 - ComfyUI_SeeCoder
 - Comfyui_segformer_b2_clothes
 - comfyui_segment_anything
 - ComfyUI_Segment_Mask
 - ComfyUI-SegMoE
 - ComfyUI_Seg_VITON
 - comfyui-self-guidance
 - ComfyUI_SendDiscord
 - ComfyUI-send-eagle-slim
 - ComfyUI-SeqImageLoader
 - ComfyUI-Serving-Toolkit
 - ComfyUI-ShadertoyGL
 - ComfyUI-Shinsplat
 - comfyUI_SillyNodes
 - ComfyUI-SimDA
 - ComfyUI-Simple-Aspect-Ratio
 - ComfyUI-SimpleCounter
 - ComfyUI_SimpleMath
 - ComfyUI_SimpleTiles
 - ComfyUI-Simply-Nodes
 - comfyui-simswap
 - ComfyUI-SizeFromArray
 - ComfyUI-SizeFromPresets
 - comfyui_slothful_attention
 - ComfyUI_smZNodes
 - ComfyUI-Sokes-Nodes
 - ComfyUI-sonar
 - ComfyUI-speech-dataset-toolkit
 - ComfyUI-SpliceTools
 - ComfyUI-StabilityAI-Suite
 - ComfyUI_StableCascadeLatentRatio
 - ComfyUI-Stable-Video-Diffusion
 - ComfyUI-stable-wildcards
 - ComfyUI-Static-Primitives
 - ComfyUI-Stereopsis
 - ComfyUI-Sticker
 - ComfyUI_StoryCreator
 - ComfyUI_StoryDiffusion
 - ComfyUI_StreamDiffusion
 - ComfyUI_StreamingT2V
 - ComfyUI_Strimmlarns_aesthetic_score
 - ComfyUi_String_Function_Tree
 - comfyui-string-tools
 - ComfyUI-string-util
 - ComfyUI-StyleGan
 - comfyui-styles-all
 - ComfyUI-Styles_CSV_Loader
 - ComfyUI-StylizePhoto-MZ
 - ComfyUI-SubjectStyle-CSV
 - ComfyUI_Substring
 - ComfyUI-sudo-latent-upscale
 - ComfyUI-SunoAI
 - ComfyUI_SUNoise
 - ComfyUI-SuperBeasts
 - Comfyui-Superprompt-Unofficial
 - ComfyUI-SUPIR
 - ComfyUI-SVD
 - ComfyUI-SVDResizer
 - ComfyUI-svd_txt2vid
 - ComfyUI-SVD-ZHO
 - comfyui-tab-handler
 - ComfyUI-TacoNodes
 - comfyui_tag_fillter
 - ComfyUI-Tara-LLM-Integration
 - ComfyUI-TCD
 - comfyui-tcd-scheduler
 - ComfyUI-TeaNodes
 - ComfyUI-TemporaryLoader
 - ComfyUI-Tensor-Operations
 - ComfyUI-Text
 - ComfyUI_TextAssets
 - ComfyUI-text-file-util
 - ComfyUI-Text_Image-Composite
 - ComfyUI-TextOnSegs
 - ComfyUI-text-overlay
 - ComfyUI-TextOverlay
 - ComfyUI-Texture-Simple
 - ComfyUI-TextUtils
 - ComfyUI_TGate
 - ComfyUI-TGu-utils
 - ComfyUI-Thumbnails
 - ComfyUI-TiledDiffusion
 - ComfyUI_TiledKSampler
 - ComfyUI_tinyterraNodes
 - ComfyUI-TITrain
 - comfyUI_TJ_NormalLighting
 - Comfyui-Toolbox
 - comfyui-tooling-nodes
 - ComfyUI_toyxyz_test_nodes
 - ComfyUI-TrackingNodes
 - ComfyUI-Trajectory
 - comfyui-transceiver
 - ComfyUI-TranscriptionTools
 - ComfyUI-Transformers
 - ComfyUI-TrashNodes-DownloadHuggingface
 - ComfyUI_TravelSuite
 - ComfyUI-Tripo
 - ComfyUI-TrollSuite
 - ComfyUI-TTS
 - ComfyUI_UltimateSDUpscale
 - comfyui-ultralytics-yolo
 - comfyui-undistort
 - ComfyUI-Universal-Styler
 - comfyui-upscale-by-model
 - ComfyUI-Upscaler-Tensorrt
 - comfyui-utility-nodes
 - ComfyUI-utils-nodes
 - ComfyUI-UVR5
 - comfyui-various
 - ComfyUI_V-Express
 - ComfyUI-Vextra-Nodes
 - ComfyUI-Video-Editing-X-Attention
 - ComfyUI-VideoHelperSuite
 - ComfyUI-Video-Matting
 - comfyui_visual_anagrams
 - ComfyUI_VisualStylePrompting
 - ComfyUI-Vivax-Nodes
 - ComfyUI_VLM_nodes
 - ComfyUI-Vsgan
 - ComfyUI_wav2lip
 - ComfyUI-WD14-Tagger
 - comfyui_webcamcapture
 - comfyui-webcam-node
 - comfyui_wfc_like
 - ComfyUI-Whisper
 - ComfyUI-WhisperX
 - ComfyUI_WordCloud
 - ComfyUI-Workflow-Encrypt
 - comfyui-workspace-manager
 - ComfyUI-XTTS
 - comfyui-yanc
 - ComfyUI_yanc
 - ComfyUI-yaResolutionSelector
 - ComfyUI_YFG_Comical
 - Comfyui-Yolov8
 - Comfyui-Yolov8-JSON
 - ComfyUI-YoloWorld-EfficientSAM
 - ComfyUI-Zero123-Porting
 - ComfyUI-ZeroShot-MTrans
 - ComfyUI_zfkun
 - comfy_vid2vid
 - ComfyWarp
 - ConCarneNode
 - conditioning_sizing_for_SDXL.py
 - ControlNet-LLLite-ComfyUI
 - cozy-utils-comfyui-nodes
 - CPlus_Ardenius
 - CrasHUtils
 - cute-comfy
 - cyberdolphin
 - darkprompts
 - deforum-comfy-nodes
 - demofusion-comfyui
 - Derfuu_ComfyUI_ModdedNodes
 - Diffusion360_ComfyUI
 - DTAIComfyImageSubmit
 - DTAIComfyLoaders
 - DTAIComfyPromptAgent
 - DTAIComfyQRCodes
 - DTAIComfyVariables
 - DTAIImageToTextNode
 - DZ-FaceDetailer
 - easy-comfy-nodes
 - eden_comfy_pipelines
 - efficiency-nodes-comfyui
 - Endless-Nodes
 - Euler-Smea-Dyn-Sampler
 - EXT_AudioManipulation.py
 - extended-saveimage-comfyui
 - facerestore_cf
 - failfast-comfyui-extensions
 - fast_video_comfyui
 - fcSuite.py
 - feidorian-ComfyNodes
 - fexli-util-node-comfyui
 - Fooocus_Nodes
 - FreeU_Advanced
 - fw_nodes.py
 - gcLatentTunnel.py
 - google_translator.py
 - graphNavigator.js
 - hakkun_nodes.py
 - Harronode
 - hd_node
 - human-parser-comfyui-node
 - IC-Light-ComfyUI-Node
 - Image-Captioning-in-ComfyUI
 - image_control
 - imageGallery.js
 - image-resize-comfyui
 - images-grid-comfy-plugin
 - img2colors-comfyui-node
 - img2txt-comfyui-nodes
 - ImgProcessing_ComfyUI
 - integrated-nodes-comfyui
 - Invisible%20Watermark.py
 - Jovimetrix
 - kb-comfyui-nodes
 - KepPromptLang
 - klinter_nodes
 - Knodes
 - komojini-comfyui-nodes
 - ksampler_gpu.py
 - LAizypainter-Exporter-ComfyUI
 - lazy-pony-prompter
 - LCM_Inpaint-Outpaint_Comfy
 - LCMSampler-ComfyUI
 - loadImageWithSubfolders.py
 - LoadLoraWithTags
 - lollms_nodes_suite
 - lora-info
 - LoRA-Merger-ComfyUI
 - Lora-Training-in-Comfy
 - LoRTnoC-ComfyUI
 - LZCNodes.py
 - m9-prompts-comfyui
 - masquerade-nodes-comfyui
 - MBM-Music-Visualizer
 - meh.py
 - MergeBlockWeighted_fo_ComfyUI
 - mikey_nodes
 - mm-comfyui-loopback
 - mm-comfyui-megamask
 - multireroute.js
 - NodeGPT
 - node_text_to_speech.py
 - noise_latent_perlinpinpin
 - NStor-ComfyUI-Translation
 - nui-suite
 - NX_PromptStyler
 - OneButtonPrompt
 - onediff_comfy_nodes
 - ostris_nodes_comfyui
 - petty-paint-comfyui-node
 - pfaeff-comfyui
 - pfg-ComfyUI
 - Plush-for-ComfyUI
 - Pomfy
 - pose-generator-comfyui-node
 - PowerNoiseSuite
 - PPF_Noise_ComfyUI
 - preview_subselection.py
 - primitive-types
 - prompt-generator-comfyui
 - prompt_quill_comfyui
 - PuLID_ComfyUI
 - qq-nodes-comfyui
 - qrng_node.py
 - queuetools
 - rembg-comfyui-node
 - rembg-comfyui-node-better
 - rgthree-comfy
 - rk-comfy-nodes
 - RUI-Nodes
 - SaltAI
 - SaltAI_Language_Toolkit
 - SaltAI_LlamaIndex
 - save-image-extended-comfyui
 - SD-Advanced-Noise
 - sd-dynamic-thresholding
 - SDFXBridgeForComfyUI
 - SD-Latent-Interposer
 - SD-Latent-Upscaler
 - sd-perturbed-attention
 - sd-ppp
 - sd-webui-color-enhance
 - SDXLAspectRatio.py
 - SDXLMixSampler.py
 - sdxl_prompt_styler
 - sdxl-recommended-res-calc
 - sdxl_utility.py
 - SeargeSDXL
 - segment_to_mask_comfyui
 - select_folder_path_easy
 - selector.py
 - sigmas_tools_and_the_golden_scheduler
 - SimpleWildcardsComfyUI
 - size-match-compositing-nodes
 - sketch2manga
 - srl-nodes
 - stability-ComfyUI-nodes
 - StableCascadeResizer
 - Stable-Diffusion-temperature-settings
 - StableZero123-comfyui
 - steerable-motion
 - style_aligned_comfy
 - suplex_comfy_nodes
 - SyrianFalconNodes.py
 - tdxh_node_comfyui
 - tiled_ksampler
 - TinkerBot-tech-for-ComfyUI-Touchpad
 - tri3d-comfyui-nodes
 - trNodes
 - TW-CUI-Util
 - ultools-comfyui
 - unwdef-nodes-comfyui
 - Vector_Sculptor_ComfyUI
 - virtuoso-nodes
 - WAS_Extras
 - was-node-suite-comfyui
 - WebDev9000-Nodes
 - webui-monaco-prompt
 - wildcards.py
 - wlsh_nodes
 - Xycuno-Oobabooga
 - yk-node-suite-comfyui
 - ymc-node-suite-comfyui
 - yugioh-presets.py
 - zhihuige-nodes-comfyui
 - ZSuite
