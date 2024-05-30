
resource "local_file" "literature" {
    filename = "local_files/art_of_war.txt"
    content = <<-EOT
        Sun Tzu said: The art of war is of vital importance to the State.

        It is a matter of life and death, a road either to safety or to
        ruin. Hence it is a subject of inquiry which can on no account be
        neglected. ${local.result}
    EOT    
}
