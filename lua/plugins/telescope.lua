return {
	{
		'nvim-telescope/telescope.nvim', tag = '0.1.8',
		dependencies = { 'nvim-lua/plenary.nvim', 'nvim-telescope/telescope-ui-select.nvim' },
		config = function()
			require("telescope").setup ({
				extensions = {
					["ui-select"] = {
						require("telescope.themes").get_dropdown {}
					}
				},
				vimgrep_arguments = {
					'~/.hbin/rg', -- Path to your specific ripgrep binary
					'--glob', '!.git/', -- You can add extra options here if you need
					'--no-ignore-vcs',
					'--hidden',  -- Include hidden files
					'--ignore-file', '/path/to/.ignore'  -- Optional: If you have a custom ignore file
				},
			})
			require("telescope").load_extension("ui-select")
		end,
	}
}
