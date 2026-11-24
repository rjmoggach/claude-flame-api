# flame module — API index (Flame 2027)

> Source: "Autodesk Flame Python: flame module" (pydoc) + per-class "Py* Attributes" help pages.

Every class lives in `import flame`. Classes are Boost.Python wrappers: none can be instantiated directly except where noted (e.g. `PyTime`, `PyResolution`, `PyExporter`) — you obtain objects from the module singletons (see [flame-module-data.md](flame-module-data.md)) and by navigating parents/children. Module-level functions (`flame.delete`, `flame.duplicate`, `flame.execute_shortcut`, …) are in [flame-module-functions.md](flame-module-functions.md). Object navigation and value semantics: [object-model.md](object-model.md).

Each class file contains: description, MRO, all methods with exact signatures (`name( (Type)arg [, (Type)opt=default]) -> ret` — bracketed args are optional keywords), read-only properties, and — where Autodesk publishes one — the documented attribute list with types and value ranges.

> **Important:** Autodesk's pydoc page predates part of the 2027 API. Always cross-check [../guides/whats-new-2027.md](../guides/whats-new-2027.md) — it adds members (metadata API, node markers/expressions, `stereo_merge`, annotations, …) and three classes with no pydoc entry: [`PyMetadataNode`](classes/PyMetadataNode.md), [`PyMetadataTimelineFX`](classes/PyMetadataTimelineFX.md), [`PyNodeMarker`](classes/PyNodeMarker.md). Affected class files carry a banner.

## Class hierarchy

```
- PyAttribute
- PyBrowser
- PyExporter
- PyFlameObject
  - PyArchiveEntry
    - PyBatchIteration
    - PyClip
      - PySequence
    - PyDesktop
    - PyFolder
    - PyLibrary
    - PyMediaHubFilesEntry
    - PyMediaHubFilesFolder
    - PyMediaHubProjectsEntry
    - PyMediaHubProjectsFolder
    - PyProject
    - PyReel
    - PyReelGroup
    - PyWorkspace
  - PyAudioTrack
  - PyBatch
  - PyCoNode
    - PyCoCameraAnalysis
    - PyCoCompass
  - PyMarker
  - PyNode
    - PyActionFamilyNode
      - PyActionNode
      - PyGMaskTracerNode
      - PyImageNode
    - PyClipNode
    - PyClrMgmtNode
    - PyCompassNode
    - PyHDRNode
    - PyInferenceNode
    - PyLensDistortionNode
    - PyMorphNode
    - PyOFXNode
    - PyPaintNode
    - PyRenderNode
      - PyWriteFileNode
    - PyTimewarpNode
  - PySegment
  - PySequenceGroup
  - PyTimelineFX
    - PyClrMgmtTimelineFX
    - PyHDRTimelineFX
    - PyTimewarpTimelineFX
    - PyTypeNode
      - PyTypeLayer
    - PyTypeTimelineFX
  - PyTrack
    - PySubtitleTrack
  - PyTransition
  - PyVersion
- PyMediaHub
- PyMediaHubFilesTabOptions
- PyMediaHubTab
  - PyMediaHubFilesTab
- PyMediaPanel
- PyMessages
- PyProjectSelector
- PyResolution
- PySearch
- PyTime
- PyTimeline
- PyUser
- PyUsers
```

## Classes

| Class | Base | Description | Methods | Properties / attributes |
|---|---|---|---|---|
| [`PyActionFamilyNode`](classes/PyActionFamilyNode.md) | PyNode | Represents an Action Family node object. | clear_schematic, connect_nodes, create_node, disconnect_nodes, encompass_nodes, get_node, organize | all_tabs, cursor_position, left_tabs, media_layers, node_types, nodes, right_tabs |
| [`PyActionNode`](classes/PyActionNode.md) | PyActionFamilyNode | Represents an Action node object. | add_media, disable_output, enable_output, export_fbx, import_abc, import_fbx, import_psd, read_abc, read_fbx | collapsed, current_node, media_nodes, name, note, note_collapsed, output_types, pos_x, pos_y, selected, selected_nodes, type |
| [`PyArchiveEntry`](classes/PyArchiveEntry.md) | PyFlameObject | Base class for any object displayed in the Media Panel. | clear_colour, commit, get_wiretap_node_id, get_wiretap_storage_id | — |
| [`PyAttribute`](classes/PyAttribute.md) |  |  | get_value, set_value | values |
| [`PyAudioTrack`](classes/PyAudioTrack.md) | PyFlameObject | Object representing an Audio Track. | copy_to_media_panel | channels, expanded, mute, selected_segments, solo, stereo |
| [`PyBatch`](classes/PyBatch.md) | PyFlameObject | This class represents a Batch Group. | append_setup, append_to_batch, append_to_setup, clear, clear_all_contexts, clear_colour, clear_context, clear_setup, close, connect_nodes, create_batch_group, create_node, create_reel, create_shelf_reel, disconnect_node, encompass_nodes, frame_all, frame_selected, get_node, go_to, import_clip, import_clips, iterate, load_setup, mimic_link, open, open_as_batch_group, organize, render, replace_setup, save, save_current_iteration, save_setup, select_nodes, set_viewport_layout | auto_key, batch_iterations, colour, colour_label, contexts, current_frame, current_iteration, current_iteration_number, current_node, cursor_position, duration, expanded, name, node_types, nodes, opened, reels, selected, selected_nodes, shelf_reels, start_frame, tags, token_name, uid |
| [`PyBatchIteration`](classes/PyBatchIteration.md) | PyArchiveEntry | This class represents a Batch Iteration. | open_as_batch_group | colour, colour_label, expanded, iteration_number, name, selected, tags, token_name, uid |
| [`PyBrowser`](classes/PyBrowser.md) |  | This class represents the file browser. | show | bit_depth, colour_space, frame_ratio, height, resize_filter, resize_mode, resolution, scaling_presets_value, scan_mode, selection, sequence_mode, width |
| [`PyClip`](classes/PyClip.md) | PyArchiveEntry | This class represents a Clip. | cache_media, change_dominance, change_start_frame, close_container, create_marker, cut, clear_cache_media, clear_renders, get_colour_space, is_rendered, open_as_sequence, open_container, reformat, render, save, update-sources | archive_date, archive_error, audio_tracks, bit_depth, cached, colour, colour_label, colour_primaries, creation_date, current_time, duration, dynamic_shot_name, essence_uid, expanded, frame_rate, has_deliverables, has_history, height, in_mark, markers, matrix_coefficients, name, original_source_uid, out_mark, proxy_resolution, ratio, sample_rate, scan_mode, selected, selected_markers, selected_segments, shot_name, source_uid, start_frame, start_time, subtitles, tags, tape_name, token_name, tokenized_shot_name, transfer_characteristics, uid, unlinked, version_uid, version_uids, versions, width |
| [`PyClipNode`](classes/PyClipNode.md) | PyNode | This class represents a Clip node. | set_version_uid | clip, colour_space, version_uid, version_uids |
| [`PyClrMgmtNode`](classes/PyClrMgmtNode.md) | PyNode | This class represents a Colour Management node. | get_context_variables, import_transform, reset_context_variables, set_context_variable | — |
| [`PyClrMgmtTimelineFX`](classes/PyClrMgmtTimelineFX.md) | PyTimelineFX | Object representing a Colour Management TimelineFX. | get_context_variables, import_transform, reset_context_variables, set_context_variable | — |
| [`PyCoCameraAnalysis`](classes/PyCoCameraAnalysis.md) | PyCoNode | This class represents the camera analysis node in the Action schematic. | analyseRange, resetAnalysis | — |
| [`PyCoCompass`](classes/PyCoCompass.md) | PyCoNode | This class represents the compass node in the Action schematic. | — | collapsed_in_manager, colour, height, name, nodes, position, selected, width |
| [`PyCoNode`](classes/PyCoNode.md) | PyFlameObject | This class represents an Action node in the Action schematic. | add_reference, assign_media, cache_range, children, parents | type |
| [`PyCompassNode`](classes/PyCompassNode.md) | PyNode | This class represents a Compass node. | — | collapsed, colour, height, name, nodes, note, note_collapsed, pos_x, pos_y, selected, type, width |
| [`PyDesktop`](classes/PyDesktop.md) | PyArchiveEntry | This class represents a Desktop. | clear, create_batch_group, create_reel_group, save | batch_groups, children, colour, colour_label, current_batch_group, destination, expanded, name, reel_groups, selected, tags, token_name, uid |
| [`PyExporter`](classes/PyExporter.md) |  | Object holding export settings. | export, get_presets_base_dir, get_presets_dir | Audio, Autodesk, BackgroundJobSettings, Distribution_Package, Image_Sequence, Movie, PresetType, PresetVisibility, Project, Sequence_Publish, Shared, Shotgun, export_all_subtitles, export_between_marks, export_subtitles_as_files, foreground, include_subtitles, keep_timeline_fx_renders, use_top_video_track, warn_on_link_unsupported, warn_on_mixed_colour_space, warn_on_no_media, warn_on_pending_render, warn_on_reimport_unsupported, warn_on_unlinked, warn_on_unrendered |
| [`PyFlameObject`](classes/PyFlameObject.md) |  | The basic type of all accessible Flame objects from the python API. | — | attributes, parent |
| [`PyFolder`](classes/PyFolder.md) | PyArchiveEntry | This class represents a Folder. | clear, create_folder, create_reel, create_reel_group, create_sequence | batch_groups, batch_iterations, children, clips, colour, colour_label, desktops, expanded, folders, name, reel_groups, reels, selected, sequences, tags, token_name, uid |
| [`PyGMaskTracerNode`](classes/PyGMaskTracerNode.md) | PyActionFamilyNode | Represents a GMask Tracer node object. | disable_output, enable_output, export_fbx, import_abc, import_fbx, read_abc, read_fbx | output_types |
| [`PyHDRNode`](classes/PyHDRNode.md) | PyNode | Object representing a HDR node. | analyze, export_DolbyVision_xml, has_trim, import_DolbyVision_xml, interpolate_trims, keep_analysis, l2_from_l8, reset_analysis, reset_trims | analysis_status, mastering_display_ids, mastering_display_info, target_display_ids, target_display_info |
| [`PyHDRTimelineFX`](classes/PyHDRTimelineFX.md) | PyTimelineFX | Object representing a HDR TimelineFX. | analyze, export_DolbyVision_xml, has_trim, import_DolbyVision_xml, interpolate_trims, keep_analysis, l2_from_l8, reset_analysis, reset_trims | analysis_status, mastering_display_ids, mastering_display_info, target_display_ids, target_display_info |
| [`PyImageNode`](classes/PyImageNode.md) | PyActionFamilyNode | Represents an Image node object. | add_media | media_nodes |
| [`PyInferenceNode`](classes/PyInferenceNode.md) | PyNode | Object representing an Inference node. | — | model_name |
| [`PyLensDistortionNode`](classes/PyLensDistortionNode.md) | PyNode | Object representing a Lens Distortion node. | calculate, import_lens_distortion | — |
| [`PyLibrary`](classes/PyLibrary.md) | PyArchiveEntry | This class represents a Library. | acquire_exclusive_access, clear, close, create_folder, create_reel, create_reel_group, create_sequence, open, release_exclusive_access | batch_groups, batch_iterations, children, clips, colour, colour_label, desktops, expanded, folders, name, opened, reel_groups, reels, selected, sequences, tags, token_name, uid |
| [`PyMarker`](classes/PyMarker.md) | PyFlameObject | Object representing a Marker. | — | colour, colour_label, comment, duration, location, locked_location, name, selected |
| [`PyMediaHub`](classes/PyMediaHub.md) |  | This class represents the MediaHub. | — | archives, files |
| [`PyMediaHubFilesEntry`](classes/PyMediaHubFilesEntry.md) | PyArchiveEntry | Object representing a clip in the MediaHub Files tabs | — | path |
| [`PyMediaHubFilesFolder`](classes/PyMediaHubFilesFolder.md) | PyArchiveEntry | Object representing a folder in the MediaHub Files tabs | — | path |
| [`PyMediaHubFilesTab`](classes/PyMediaHubFilesTab.md) | PyMediaHubTab | This class represents the MediaHub Files tab. | — | options |
| [`PyMediaHubFilesTabOptions`](classes/PyMediaHubFilesTabOptions.md) |  | This class represents the MediaHub Files tab options. | set_tagged_colour_space | bit_depth, cache_and_proxies_all_versions, cache_mode, frame_ratio, height, multi_channel_mode, pixel_ratio, proxies_mode, resize_filter, resize_mode, resolution, scaling_presets_value, scan_mode, sequence_mode, width |
| [`PyMediaHubProjectsEntry`](classes/PyMediaHubProjectsEntry.md) | PyArchiveEntry | Object representing a clip in the MediaHub Projects tabs | — | path, uid |
| [`PyMediaHubProjectsFolder`](classes/PyMediaHubProjectsFolder.md) | PyArchiveEntry | Object representing a folder in the MediaHub Projects tabs | — | path, uid |
| [`PyMediaHubTab`](classes/PyMediaHubTab.md) |  | This class represents a MediaHub tab. | get_path, set_path | — |
| [`PyMediaPanel`](classes/PyMediaPanel.md) |  | This class represents the Media Panel. | copy, move | dual, full_height, full_width, selected_entries, visible |
| [`PyMessages`](classes/PyMessages.md) |  | Module handling message bar in application UI. | clear_console, show_in_console, show_in_dialog | — |
| [`PyMorphNode`](classes/PyMorphNode.md) | PyNode | Object representing a Morph node. | set_mix_to_range | — |
| [`PyNode`](classes/PyNode.md) | PyFlameObject | Object representing a Node. | cache_range, clear_schematic_colour, delete, duplicate, load_node_setup, save_node_setup, set_context, clear_schematic_colour | bypass, collapsed, colour_space, input_sockets, name, note, note_collapsed, output_sockets, pos_x, pos_y, selected, shot_name, sockets, type |
| [`PyOFXNode`](classes/PyOFXNode.md) | PyNode | Object representing a OpenFX node. | change_plugin | bypass, collapsed, name, note, note_collapsed, plugin_name, pos_x, pos_y, preserve_input_colour_space, selected, type |
| [`PyPaintNode`](classes/PyPaintNode.md) | PyNode | Object representing a Paint node. | add_source | collapsed, name, note, note_collapsed, pos_x, pos_y, selected, type |
| [`PyProject`](classes/PyProject.md) | PyArchiveEntry | Object representing a Project. | create_shared_library, export_ocio_config, get_context_variables, refresh_shared_libraries, reload_ocio_config, reset_context_variables, set_context_variable | action_colour_space, current_workspace, description, media_folder, name, nickname, project_folder, project_name, setups_folder, shared_libraries, shotgrid_project_name, working_colour_space, workspaces_count |
| [`PyProjectSelector`](classes/PyProjectSelector.md) |  | Object representing the Project manager. | — | current_project |
| [`PyReel`](classes/PyReel.md) | PyArchiveEntry | Object representing a Reel. | clear, create_sequence, save | children, clips, colour, colour_label, expanded, name, selected, sequences, tags, token_name, type, uid |
| [`PyReelGroup`](classes/PyReelGroup.md) | PyArchiveEntry | Object representing a Reel Group. | clear, create_reel, save | children, colour, colour_label, expanded, name, reels, selected, tags, token_name, uid |
| [`PyRenderNode`](classes/PyRenderNode.md) | PyNode | This class represents a Render node. | set_channel_name | channels |
| [`PyResolution`](classes/PyResolution.md) |  | Object representing a resolution | — | bit_depth, frame_ratio, height, resolution, scan_mode, width |
| [`PySearch`](classes/PySearch.md) |  | This class represents the search. | activate_search_result, search_results, set_tool_favorite, set_tool_hidden, set_tool_weight | use_weight |
| [`PySegment`](classes/PySegment.md) | PyFlameObject | Object representing a Segment. | change_start_frame, clear_colour, connected_segments, copy_to_media_panel, create_connection, create_effect, create_marker, create_unlinked_segment, duplicate_source, get_colour_space, is_rendered, match, remove_connection, set_gap_bars, set_gap_colour, set_matte_channel, set_rgb_channel, set_version_uid, shared_source_segments, slide_keyframes, slip, smart_replace, smart_replace_media, sync_connected_segments, trim_head, trim_tail | colour, colour_label, comment, container_clip, dynamic_comment, dynamic_name, dynamic_shot_name, effect_types, effects, file_path, groups, head, hidden, markers, matte_channel, matte_channels, matte_mode, name, original_source_uid, record_duration, record_in, record_out, rgb_channel, rgb_channels, selected, selected_markers, shot_name, source_audio_track, source_bit_depth, source_cached, source_colour_primaries, source_duration, source_essence_uid, source_frame_rate, source_has_history, source_height, source_in, source_matrix_coefficients, source_name, source_out, source_ratio, source_sample_rate, source_scan_mode, source_transfer_characteristics, source_uid, source_unlinked, source_width, start_frame, tags, tail, tape_name, tokenized_comment, tokenized_name, tokenized_shot_name, type, version_uid, version_uids |
| [`PySequence`](classes/PySequence.md) | PyClip | Object representing a Sequence. | copy_selection_to_media_panel, create_audio, create_container, create_group, create_subtitle, create_version, extract_selection_to_media_panel, import_subtitles_file, insert, lift_selection_to_media_panel, open, overwrite | colour, colour_label, current_time, expanded, groups, in_mark, name, out_mark, primary_track, secondary_track, selected, selected_markers, selected_segments, start_time, tags, token_name, uid |
| [`PySequenceGroup`](classes/PySequenceGroup.md) | PyFlameObject | Object representing a Group in a Sequence. | add, remove | segments |
| [`PySubtitleTrack`](classes/PySubtitleTrack.md) | PyTrack | Object representing a Subtitle Track. | export_as_avid_txt_file, export_as_srt_file | — |
| [`PyTime`](classes/PyTime.md) |  | Object representing a time unit | — | frame, frame_rate, relative_frame, timecode |
| [`PyTimeline`](classes/PyTimeline.md) |  | This class represents the Timeline. | — | clip, current_effect, current_marker, current_segment, current_transition, type |
| [`PyTimelineFX`](classes/PyTimelineFX.md) | PyFlameObject | Object representing a TimelineFX. | clear_maps_cache_media, load_setup, save_setup, slide_keyframes, sync_connected_segments | bypass, has_maps_cache_media, type |
| [`PyTimewarpNode`](classes/PyTimewarpNode.md) | PyNode | Object representing a Timewarp node. | get_duration_timing, get_speed, get_timing, get_speed_timing, set_speed, set_timing | — |
| [`PyTimewarpTimelineFX`](classes/PyTimewarpTimelineFX.md) | PyTimelineFX | Object representing a Timewarp TimelineFX. | get_duration_timing, get_speed, get_speed_timing, get_timing, set_speed, set_timing | — |
| [`PyTrack`](classes/PyTrack.md) | PyFlameObject | Object representing a Track. | copy_to_media_panel, cut, insert_transition | hidden, locked, name, segments, selected_segments, stereo_linked, transitions |
| [`PyTransition`](classes/PyTransition.md) | PyFlameObject | Object representing a Transition. | set_dissolve_to_from_colour, set_fade_to_from_silence, set_transition, slide | in_offset, record_time, type |
| [`PyTypeLayer`](classes/PyTypeLayer.md) | PyTypeNode | Object representing a Type Layer. | — | type |
| [`PyTypeNode`](classes/PyTypeNode.md) | PyTimelineFX | Object representing a Type TimelineFX. | add_layer, append_type_setup | layers |
| [`PyTypeTimelineFX`](classes/PyTypeTimelineFX.md) | PyTimelineFX | Object representing a Type TimelineFX. | add_layer, append_type_setup | layers |
| [`PyUser`](classes/PyUser.md) |  | Object representing a User. | — | name, nickname, shortcuts_profile |
| [`PyUsers`](classes/PyUsers.md) |  | Object representing the User manager. | — | current_user |
| [`PyVersion`](classes/PyVersion.md) | PyFlameObject | Object representing a Version. | copy_to_media_panel, create_track, import_DolbyVision_xml | expanded, selected_segments, stereo, tracks |
| [`PyWorkspace`](classes/PyWorkspace.md) | PyArchiveEntry | Object representing a Workspace. | create_library, replace_desktop, set_desktop_reels, set_freeform | colour, colour_label, current_reel_group, desktop, expanded, libraries, name, selected, tags, token_name, uid |
| [`PyWriteFileNode`](classes/PyWriteFileNode.md) | PyRenderNode | This class represents a WriteFile node. | get_resolved_media_path | — |
