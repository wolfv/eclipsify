languageTemplate=R'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<project>
	<configuration id="cdt.managedbuild.toolchain.gnu.macosx.base.205247326" name="Default">
		<extension point="org.eclipse.cdt.core.LanguageSettingsProvider">
			<provider copy-of="extension" id="org.eclipse.cdt.ui.UserLanguageSettingsProvider"/>
			<provider-reference id="org.eclipse.cdt.core.ReferencedProjectsLanguageSettingsProvider" ref="shared-provider"/>
			<provider class="org.eclipse.cdt.managedbuilder.language.settings.providers.GCCBuildCommandParser" id="org.eclipse.cdt.managedbuilder.core.GCCBuildCommandParser" keep-relative-paths="false" name="CDT GCC Build Output Parser" parameter="(.*gcc)|(.*[gc]\+\+)|(.*clang)" prefer-non-shared="true"/>
			<provider-reference id="org.eclipse.cdt.managedbuilder.core.GCCBuiltinSpecsDetector" ref="shared-provider"/>
			<provider-reference id="org.eclipse.cdt.managedbuilder.core.MBSLanguageSettingsProvider" ref="shared-provider"/>
		</extension>
	</configuration>
</project>
'''
def get():
    return languageTemplate