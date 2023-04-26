<!-- included start from vtysh-generic-interface.xml.i -->
<tagNode name="interface">
  <properties>
    <help>Show information about specific interface</help>
    <completionHelp>
      <script>${ngnos_completion_dir}/list_interfaces</script>
    </completionHelp>
  </properties>
  <command>${ngnos_op_scripts_dir}/vtysh_wrapper.sh $@</command>
</tagNode>
<!-- included end -->
