Source
│     ├─ A302
│     │  ├─ A302.Build.cs
│     │  ├─ A302.cpp
│     │  ├─ A302.h
│     │  ├─ AI
│     │  │  ├─ Dummy.cpp
│     │  │  └─ Dummy.h
│     │  ├─ Animation
│     │  │  ├─ MyAnimInstance.cpp
│     │  │  └─ MyAnimInstance.h
│     │  ├─ Character
│     │  │  ├─ Components
│     │  │  │  ├─ CombatStatusComponent.cpp
│     │  │  │  ├─ CombatStatusComponent.h
│     │  │  │  ├─ InteractComponent.cpp
│     │  │  │  ├─ InteractComponent.h
│     │  │  │  ├─ KnifeAutoTestComponent.cpp
│     │  │  │  ├─ KnifeAutoTestComponent.h
│     │  │  │  ├─ MaliceComponent.cpp
│     │  │  │  ├─ MaliceComponent.h
│     │  │  │  ├─ QuickSlotComponent.cpp
│     │  │  │  ├─ QuickSlotComponent.h
│     │  │  │  ├─ QuickSlotComponent.Internal.cpp
│     │  │  │  └─ QuickSlotComponent.UI.cpp
│     │  │  ├─ DummyCharacter.cpp
│     │  │  ├─ DummyCharacter.h
│     │  │  ├─ MyCharacter.cpp
│     │  │  ├─ MyCharacter.h
│     │  │  ├─ MyPlayerController.cpp
│     │  │  ├─ MyPlayerController.h
│     │  │  └─ MyPlayerController.Resolution.cpp
│     │  ├─ GameData
│     │  │  ├─ ItemDefinition.cpp
│     │  │  ├─ ItemDefinition.h
│     │  │  ├─ ItemInstance.cpp
│     │  │  ├─ ItemInstance.h
│     │  │  └─ ItemTypes.h
│     │  ├─ GameMode
│     │  │  ├─ A302GameInstance.cpp
│     │  │  ├─ A302GameInstance.h
│     │  │  ├─ A302GameMode.cpp
│     │  │  ├─ A302GameMode.h
│     │  │  ├─ A302GameState.cpp
│     │  │  ├─ A302GameState.h
│     │  │  ├─ A302PlayerState.cpp
│     │  │  ├─ A302PlayerState.h
│     │  │  ├─ InGameGameMode.cpp
│     │  │  ├─ InGameGameMode.h
│     │  │  ├─ LobbyGameMode.cpp
│     │  │  └─ LobbyGameMode.h
│     │  ├─ GamePlay
│     │  │  └─ Items
│     │  │     ├─ BaseItem.cpp
│     │  │     ├─ BaseItem.h
│     │  │     ├─ ItemKnife.cpp
│     │  │     ├─ ItemKnife.h
│     │  │     ├─ ItemMalice.cpp
│     │  │     ├─ ItemMalice.h
│     │  │     ├─ ItemShield.cpp
│     │  │     ├─ ItemShield.h
│     │  │     ├─ ItemTimeKnife.cpp
│     │  │     └─ ItemTimeKnife.h
│     │  ├─ Interface
│     │  │  ├─ InteractableInterface.cpp
│     │  │  ├─ InteractableInterface.h
│     │  │  └─ UsableItem.h
│     │  ├─ Manager
│     │  │  ├─ ItemActionFactory.cpp
│     │  │  ├─ ItemActionFactory.h
│     │  │  ├─ SpawnManager.cpp
│     │  │  └─ SpawnManager.h
│     │  ├─ Network
│     │  │  ├─ WebSocketManager.cpp
│     │  │  └─ WebSocketManager.h
│     │  ├─ Object
│     │  │  ├─ BaseInteractable.cpp
│     │  │  ├─ BaseInteractable.h
│     │  │  ├─ SpawnArea.cpp
│     │  │  └─ SpawnArea.h
│     │  ├─ UI
│     │  │  ├─ ChatMessageItem.cpp
│     │  │  ├─ ChatMessageItem.h
│     │  │  ├─ ChatWidget.cpp
│     │  │  ├─ ChatWidget.h
│     │  │  ├─ EnterRoomPopup.cpp
│     │  │  ├─ EnterRoomPopup.h
│     │  │  ├─ LobbyWidget.cpp
│     │  │  ├─ LobbyWidget.h
│     │  │  ├─ PlayerListItem.cpp
│     │  │  ├─ PlayerListItem.h
│     │  │  ├─ RoomListItem.cpp
│     │  │  ├─ RoomListItem.h
│     │  │  ├─ RoomListPopup.cpp
│     │  │  ├─ RoomListPopup.h
│     │  │  ├─ WaitingRoomWidget.cpp
│     │  │  └─ WaitingRoomWidget.h
│     │  └─ Voice
│     │     ├─ PrivateVoiceChatComponent.cpp
│     │     ├─ PrivateVoiceChatComponent.h
│     │     ├─ Strategy
│     │     │  ├─ DistanceVoiceChatStrategy.cpp
│     │     │  ├─ DistanceVoiceChatStrategy.h
│     │     │  ├─ LobbyVoiceChatStrategy.cpp
│     │     │  ├─ LobbyVoiceChatStrategy.h
│     │     │  ├─ VoiceChatStrategyBase.cpp
│     │     │  └─ VoiceChatStrategyBase.h
│     │     ├─ VoiceAudioReceiver.cpp
│     │     ├─ VoiceAudioReceiver.h
│     │     ├─ VoiceCaptureProcessor.cpp
│     │     ├─ VoiceCaptureProcessor.h
│     │     ├─ VoiceChatMode.h
│     │     ├─ VoiceNetworkClient.cpp
│     │     └─ VoiceNetworkClient.h
│     ├─ A302.Target.cs
│     ├─ A302Editor.Target.cs
│     └─ A302Server.Target.cs

현재 프로젝트의 c++ 코드들이 모여있는 패키지 구조를 확인하고 전체적으로 모듈화와 리팩터링이 잘 되어있는지 점검해줄 수 있어?