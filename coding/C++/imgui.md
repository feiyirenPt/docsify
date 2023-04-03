---
title: imgui  
date: 2022-01-07  
tags: C++  
---

## font
- 微软雅黑.ttf可以支持中文
- Jetbrain的字体似乎不可以

?> 确保传入imgui的是utf-8

?> unicode是字符编码集合,utf-*是存储方式

[官方文档](https://github.com/ocornut/imgui/blob/master/docs/FONTS.md)

```cpp
io.Fonts->AddFontFromFileTTF(R"(font/微软雅黑.ttf)", 30.0f, nullptr,
io.Fonts->GetGlyphRangesChineseFull());
io.Fonts->Build();
```


## 常用组件
- text
```cpp
ImGui::Text("Hello, world!");
```

- bullettext
```cpp
ImGui::BulletText("Return to input text into a widget.");
```

- slide
```cpp
float f;
ImGui::SliderFloat("float", &f, 0.0f, 1.0f);
```

- color
```cpp
ImVec4 clear_color = ImVec4(0.45f, 0.55f, 0.60f, 1.00f);
ImGui::ColorEdit3("clear color", (float*)&clear_color);
```

- checkbox
```cpp
ImGui::Checkbox("Demo Window", &show_demo_window);
```
- button
```cpp 
int counter = 0;
if (ImGui::Button("Button")) 
    counter++;
ImGui::SameLine();
ImGui::Text("counter = %d", counter);
ImGui::End();
```

- format
```cpp
ImGui::Text("Application average %.3f ms/frame (%.1f FPS)",1000.0f / ImGui::GetIO().Framerate, ImGui::GetIO().Framerate);
```

- [menu bar](https://github.com/ocornut/imgui/blob/d7c8516a4b848c0291e3d75b627c0843f515f591/imgui_demo.cpp#L351-L394)
```cpp
if (ImGui::BeginMenuBar()) {
        if (ImGui::BeginMenu("File")) {
            if (ImGui::MenuItem("Open..", "Ctrl+O")) {
                spdlog::info("Open");
            }
            if (ImGui::MenuItem("Save", "Ctrl+S")) {
            }
            if (ImGui::MenuItem("Close", "Ctrl+W")) {
            }
            ImGui::EndMenu();
        }
        ImGui::EndMenuBar();
    }
```
- inputtext
```cpp
static char str0[128] = "Hello, world!";
ImGui::InputText("input text", str0, IM_ARRAYSIZE(str0));

static char str1[128] = "";
ImGui::InputTextWithHint("input text (w/ hint)", "enter text here", str1, IM_ARRAYSIZE(str1));
```

- table
```cpp
if (ImGui::BeginTable("split", 3))
        {
            ImGui::TableNextColumn(); ImGui::Checkbox("No titlebar", &no_titlebar);
            ImGui::TableNextColumn(); ImGui::Checkbox("No scrollbar", &no_scrollbar);
            ImGui::TableNextColumn(); ImGui::Checkbox("No menu", &no_menu);
            ImGui::TableNextColumn(); ImGui::Checkbox("No move", &no_move);
            ImGui::TableNextColumn(); ImGui::Checkbox("No resize", &no_resize);
            ImGui::TableNextColumn(); ImGui::Checkbox("No collapse", &no_collapse);
            ImGui::TableNextColumn(); ImGui::Checkbox("No close", &no_close);
            ImGui::TableNextColumn(); ImGui::Checkbox("No nav", &no_nav);
            ImGui::TableNextColumn(); ImGui::Checkbox("No background", &no_background);
            ImGui::TableNextColumn(); ImGui::Checkbox("No bring to front", &no_bring_to_front);
            ImGui::TableNextColumn(); ImGui::Checkbox("Unsaved document", &unsaved_document);
            ImGui::EndTable();
        }
```

## 常用控件

| 控件名                  | 用途                     |
| ----------------------- | ------------------------ |
| Popup                   | 弹窗                     |
| Menu                    | 菜单                     |
| MainMenuBar             | 主菜单框                 |
| Popup                   | 弹窗                     |
| Text                    | 文本                     |
| TextDisabled            | 不可编辑文本，浅色底     |
| TextColored             | 带颜色的文本             |
| BulletText              | 前面带个●的文本          |
| SameLine                | 使同一行                 |
| Separator               | 画一条横线分割           |
| RadioButton             | 带一个可点击圆圈的选择项 |
| ArrowButton             | 带左右方向的按钮         |
| Combo                   | 带下拉的选择框           |
| AlignTextToFramePadding | 文本与控件框对齐         |
| CheckBox                | 带方框的选择框           |

### reference
- [ImGui渲染流程及常用控件总结](https://blog.csdn.net/rasine_liu/article/details/127624805)
- [doc](https://oprypin.github.io/crystal-imgui/ImGui.html)