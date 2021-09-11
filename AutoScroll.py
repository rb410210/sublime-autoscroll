import sublime
import sublime_plugin


class AutoScroll(sublime_plugin.TextCommand):
    def scroll(self, edit):
        old_position = self.view.viewport_position()
        layout_height = self.view.layout_extent()[1]
        new_y = old_position[1] + (layout_height / 1000)
        self.view.set_viewport_position((old_position[0], new_y), True)

    def run(self, edit):
    	for x in range(1000):
	    	sublime.set_timeout_async(lambda: self.scroll(self), (x * 5 * 60))
