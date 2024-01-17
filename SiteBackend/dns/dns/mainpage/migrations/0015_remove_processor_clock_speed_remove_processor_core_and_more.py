# Generated by Django 5.0.1 on 2024-01-16 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0014_remove_motherboard_active_cooling_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processor',
            name='clock_speed',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='core',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='heat_release',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='l2_cache_size',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='l3_cache_size',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='max_clock_speed',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='max_ram',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='max_temperature',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='num_channels',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='release_year',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='technical_process',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='threads',
        ),
        migrations.RemoveField(
            model_name='processor',
            name='virtualization',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='additional_power_connectors',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='alu',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='connection_connector_form_factor',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='connection_interface',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='cooling_type',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='designed_for_mining',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='displayport_version',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='effective_memory_frequency',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='graphics_card_thickness',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='hdmi_version',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='max_memory_bandwidth',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='max_resolution',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='memory_type',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='microarchitecture',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='num_fans_installed',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='num_pci_express_lines',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='num_rasterization_blocks',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='num_texture_blocks',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='power_consumption',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='ray_tracing_support',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='recommended_power_supply',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='rgb_backlight_synchronization',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='rt_cores',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='standard_clock_speed',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='technical_process',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='tensor_kernels',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='turbo_clock_speed',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='video_card_element_highlighting',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='video_card_length',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='video_card_width',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='video_connectors',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='video_memory_size',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='weight',
        ),
    ]